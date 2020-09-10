# coding:utf-8
import datetime
import sys

import configobj
import pymysql
import json
import os
from time import time

import sqlparse

from py_kd_data_common_proj.ds_utils.ds_pymysql_util import fetch_all, execute_sql

config_path = os.getcwd() + '/../james_config/tct_dc_config.conf'
CO = configobj.ConfigObj(config_path)


def replaceWord(str):
    return str.replace("'", "TOK_SINGLE_QUOTE").replace("\n", "TOK_BACKSLASH_N").replace("\r",
                                                                                         "TOK_BACKSLASH_R").replace(
        "$", "TOK_DOLLAR").replace(",", "TOK_COMMA")


def read_from_table(DB_COR, lineage_id=246):
    sql_select = "SELECT lineage_str FROM developer.txkd_dc_hive_lineage_log_daily where ftime=20200817 and id=%s;" % lineage_id
    results = fetch_all(DB_COR,
                        sql_select)
    return results


def process_txkd_dc_hive_lineage_info(lineage, hive_lineage_log_id, DB_COR, DB_CONN):
    print(f"hive_lineage_log_id={hive_lineage_log_id}")
    print(lineage)
    print("-" * 160)

    clean_lineage = " ".join(lineage.split())

    data_dict = json.loads(clean_lineage)

    update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 查询sql
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
    # i = 100
    # j = 100

    insert_records = []

    edges = data_dict["edges"]

    for elem in edges:
        sources = elem["sources"]

        if not sources:
            sources = list()
            sources.append(-99)
            # print("\t--sources is null")
            # print(sources)
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

                    print("-" * 160)
                    print(f"dest_column_name={dest_column_name}")
                    print("-" * 160)
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
                        replaceWord(full_src_field),
                        replaceWord(full_des_field),
                        replaceWord(rel),
                        replaceWord(src_field),
                        replaceWord(des_field),
                        replaceWord(src_table),
                        replaceWord(des_table),
                        update_time,
                        replaceWord(sql_format),
                        -1, ext)

                    insert_records.append(sql_record)
                    # print('*' * 160)
                    # print(insert_records)SELECT count(1) cnt
                    # FROM txkd_dc_hive_lineage_rel_prod_daily
                    # WHERE locate(".", full_des_field)>0;
                    # print("\n")

    if insert_records and len(insert_records) > 0:
        DB_COR.executemany(
            "insert into txkd_dc_hive_lineage_rel(full_src_field, full_des_field, rel, src_field, des_field, src_table, des_table, update_time, sql_format, hive_lineage_log_id, ext) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            insert_records)

        DB_CONN.commit()

        insert_records.clear()


def main():
    DB_HOST = CO['LOCAL_DB']['host']
    DB_USER = CO['LOCAL_DB']['user']
    DB_PASSWD = CO['LOCAL_DB']['passwd']
    DB_DB = CO['LOCAL_DB']['db']
    DB_PORT = CO['LOCAL_DB'].as_int('port')

    DB_CONN = pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD,
                              db=DB_DB,
                              port=DB_PORT,
                              charset='utf8')

    # # 解析单条点边关系
    # lineage_id = 1664
    # DB_COR = DB_CONN.cursor()
    # results = read_from_table(DB_COR, lineage_id)
    # lineage = str(results[0][0])
    # print(f"{lineage}")
    # print('-' * 160)
    # process_txkd_dc_hive_lineage_info(lineage,
    #                                   lineage_id, DB_COR, DB_CONN)

    ### 批量解析
    # for lineage_id in range(1, 23):
    for lineage_id in range(1, 13313):
        print(f"lineage_id={lineage_id}")

        DB_COR = DB_CONN.cursor()
        results = read_from_table(DB_COR, lineage_id)
        print(results)
        lineage = results[0][0]
        # print(f"{lineage}")
        # print('-'*160)
        process_txkd_dc_hive_lineage_info(lineage, lineage_id, DB_COR, DB_CONN)

    sys.exit(0)


if __name__ == '__main__':
    start = time()
    main()
    stop = time()
    print(str(stop - start) + "秒")
