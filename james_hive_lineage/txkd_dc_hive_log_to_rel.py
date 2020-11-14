# coding:utf-8
import datetime
import multiprocessing
import sys

import configobj
import pymysql
import json
import os
from datetime import datetime, timedelta
import time

import sqlparse

from py_kd_data_common_proj.ds_utils.ds_pymysql_util import fetch_all, execute_sql


# YYYYMMDD -> YYYY-MM-DD
def add_hyphen_on_date(data_date):
    hyphen_data_date = datetime.strptime(
        data_date, '%Y%m%d').strftime('%Y-%m-%d')

    return hyphen_data_date


# 20200815
def get_delta_date_str(delta, date):
    if date:
        now = datetime.strptime(date, '%Y%m%d')
    else:
        now = datetime.now()
    print(f"now={now}")

    delta_days = timedelta(days=1) * delta

    ret = (now + delta_days).strftime("%Y%m%d")

    return ret


def replace_word(str):
    return str.replace("'", "TOK_SINGLE_QUOTE").replace("\n", "TOK_BACKSLASH_N").replace("\r",
                                                                                         "TOK_BACKSLASH_R").replace(
        "$", "TOK_DOLLAR").replace(",", "TOK_COMMA")


def get_hive_log_from_table(data_date, lineage_id, partition_n):
    sql_select = f"SELECT lineage_str, id, lineage_str_sha FROM developer.txkd_dc_hive_lineage_log_daily WHERE ftime={data_date}"
    if lineage_id and lineage_id != -1:
        sql_select = f"{sql_select} AND id={lineage_id}"
    if partition_n is not None:
        sql_select = f"{sql_select} AND id % 5={partition_n}"
    print(f"{'-' * 16} get_hive_log_from_table(lineage_id): {'-' * 16}")
    print(f"sql_select={sql_select}")

    db_cor = _DB_CONN.cursor()

    db_cor.execute(sql_select)

    return db_cor.fetchall()


def process_txkd_dc_hive_lineage_info(data_date, hive_log_id, partition_n):
    print(f"{'-' * 16} process_txkd_dc_hive_lineage_info(lineage_id): {'-' * 16}")
    record = get_hive_log_from_table(data_date, -1, partition_n)

    for i in range(1, record.__len__()):
        lineage_str = str(record[i][0])
        lineage_id = str(record[i][1])
        lineage_str_sha = str(record[i][2])
        print(f"lineage_id={lineage_id} -- lineage_str_sha={lineage_str_sha}")
        print(f"lineage_str={lineage_str}")

        clean_lineage_str = " ".join(lineage_str.split())

        data_dict = json.loads(clean_lineage_str)

        update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 在Hive中执行的sql
        query_sql = data_dict["queryText"]
        sql_format = sqlparse.format(query_sql, reindent=True, keyword_case='upper')

        # 所有顶点装入字典
        vertices = data_dict["vertices"]
        vertices_dict = {}
        for elem in vertices:
            key = elem["id"]
            type = elem["vertexType"]
            value = elem["vertexId"]
            vertices_dict[key] = (type, value)

        vertices_dict[-99] = ('_USER_DEFINED', "_USER_DEFINED")

        # 解析边的关系
        insert_records = []

        edges = data_dict["edges"]

        for elem in edges:
            sources = elem["sources"]

            if not sources:
                sources = list()
                sources.append(-99)
            targets = elem["targets"]
            edgeType = elem["edgeType"]

            ## TODO
            if "expression" in elem:
                # expression = base64.decodebytes(elem["expression"].encode()).decode('utf-8')
                expression = elem["expression"]
            else:
                expression = "NONE_TRANSFORM"

            # print(f"sources={sources} -> targets={targets} @ edgeType={edgeType}: expression={expression}")

            if edgeType == "PROJECTION":
                for target in targets:
                    if vertices_dict[target][0] == "COLUMN":
                        dest_column_name = vertices_dict[target][1]
                    elif vertices_dict[target][0] == "TABLE":
                        dest_column_name = vertices_dict[target][1] + "." + expression

                    for source in sources:
                        if source == -99:
                            origin_column_name = "_USER_DEFINED._USER_DEFINED._USER_DEFINED"
                        if vertices_dict[source][0] == "COLUMN":
                            origin_column_name = vertices_dict[source][1]
                        elif vertices_dict[source][0] == "TABLE":
                            origin_column_name = vertices_dict[source][1] + "." + expression

                        # 过滤过长的字符串
                        print(f"\t{len(origin_column_name)}")
                        if len(origin_column_name) > 200:
                            continue

                        # ## 打印点边关系
                        # print(
                        #     f"{origin_column_name} -> {dest_column_name} ->@ {expression} << {origin_column_name.rsplit('.', 1)[0]} -> {dest_column_name.rsplit('.', 1)[0]} << {origin_column_name.rsplit('.', 1)[1]} -> {dest_column_name.rsplit('.', 1)[1]}")
                        # print('-' * 160)
                        # print(f"\t{query_sql}")

                        # sql_base64_encode = replaceWord(str(base64.encodebytes(sql_format.encode())))
                        # print(f"sql_base64_encode=\t{sql_base64_encode}")

                        # print("-" * 160)
                        # print(f"dest_column_name={dest_column_name}")
                        # print("-" * 160)
                        (full_src_field, full_des_field, rel, src_field, des_field, src_table, des_table, update_time,
                         sql_format, hive_lineage_log_id, ext) = (origin_column_name, dest_column_name, expression,
                                                                  origin_column_name.rsplit('.', 1)[1],
                                                                  dest_column_name.rsplit('.', 1)[
                                                                      1] if dest_column_name.__contains__(
                                                                      ".") else dest_column_name,
                                                                  origin_column_name.rsplit('.', 1)[0],
                                                                  dest_column_name.rsplit('.', 1)[0],
                                                                  update_time, sql_format, id, '')

                        sql_record = (
                            int(data_date),
                            replace_word(full_src_field),
                            replace_word(full_des_field),
                            replace_word(rel),
                            replace_word(src_field),
                            replace_word(des_field),
                            replace_word(src_table),
                            replace_word(des_table),
                            update_time,
                            replace_word(sql_format),
                            lineage_id, ext)

                        insert_records.append(sql_record)
                        # print('*' * 160)
                        # print(insert_records)SELECT count(1) cnt
                        # FROM txkd_dc_hive_lineage_rel_prod_daily
                        # WHERE locate(".", full_des_field)>0;
                        # print("\n")

    db_cor = _DB_CONN.cursor()
    if insert_records and len(insert_records) > 0:
        db_cor.executemany(
            "insert into txkd_dc_hive_lineage_rel_prod_daily(ftime, full_src_field, full_des_field, rel, src_field, des_field, src_table, des_table, update_time, sql_format, hive_lineage_log_id, ext) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            insert_records)

        _DB_CONN.commit()

        insert_records.clear()


def main():
    job_date = '20200816'
    data_date = get_delta_date_str(-1, job_date)
    hyphen_job_date = add_hyphen_on_date(job_date)
    hyphen_data_date = add_hyphen_on_date(data_date)
    print(f"hyphen_job_date={hyphen_job_date}\nhyphen_data_date={hyphen_data_date}")

    # process_txkd_dc_hive_lineage_info(data_date, hive_log_id=-1, partition_n=0)

    pool = multiprocessing.Pool(processes=_TOTAL_PARTITION_CNT)
    for i in range(0, _TOTAL_PARTITION_CNT):
        pool.apply_async(func=process_txkd_dc_hive_lineage_info, args=(data_date, -1, i))
    pool.close()
    pool.join()


if __name__ == '__main__':
    _CONFIG_PATH = os.getcwd() + '/../james_config/tct_dc_config.conf'
    _CO = configobj.ConfigObj(_CONFIG_PATH)

    _DB_HOST = _CO['LOCAL_DB']['host']
    _DB_USER = _CO['LOCAL_DB']['user']
    _DB_PASSWD = _CO['LOCAL_DB']['passwd']
    _DB_DB = _CO['LOCAL_DB']['db']
    _DB_PORT = _CO['LOCAL_DB'].as_int('port')

    _DB_CONN = pymysql.connect(host=_DB_HOST, user=_DB_USER, passwd=_DB_PASSWD,
                               db=_DB_DB,
                               port=_DB_PORT,
                               charset='utf8')

    _TOTAL_PARTITION_CNT = 5

    _JOB_START = time.time()
    main()
    _JOB_STOP = time.time()
    print(str(_JOB_STOP - _JOB_START) + "秒")

    sys.exit(0)
