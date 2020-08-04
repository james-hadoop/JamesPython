# coding:utf-8
import datetime
import sys

import configobj
import pymysql
import json
import os
import re
import base64

import sqlparse
from pyecharts import options as opts
from pyecharts.charts import Graph

from py_kd_data_common_proj.ds_utils.ds_pymysql_util import fetch_all, execute_sql

config_path = os.getcwd() + '/../james_config/james_config.conf'
CO = configobj.ConfigObj(config_path)


def write_to_table(DB_COR, DB_CONN, full_src_field, full_des_field, rel, src_field, des_field, src_table, des_table,
                   update_time, sql_format, hive_lineage_log_id, ext):
    update_name = 'jamesqjiang'
    value = 'i am a value@' + update_time
    ext = '{}'

    """
        INSERT INTO txkd_dc_hive_lineage_rel (full_src_field, full_des_field, rel, src_field, des_field, src_table, des_table, update_time, sql_format, hive_lineage_log_id, ext) VALUES ('', '', '', '', '', '', '', '', '', '', '');

    """

    convert_rel = rel.replace("'", "TOK_SINGLE_QUOTE").replace("$", "TOK_DOLLAR").replace(",", "TOK_COMMA")
    convert_full_src_field = full_src_field.replace("'", "TOK_SINGLE_QUOTE").replace("$", "TOK_DOLLAR").replace(",",
                                                                                                            "TOK_COMMA")
    convert_full_des_field = full_des_field.replace("'", "TOK_SINGLE_QUOTE").replace("$", "TOK_DOLLAR").replace(",",
                                                                                                            "TOK_COMMA")
    convert_src_field = src_field.replace("'", "TOK_SINGLE_QUOTE").replace("$", "TOK_DOLLAR").replace(",", "TOK_COMMA")
    convert_des_field = des_field.replace("'", "TOK_SINGLE_QUOTE").replace("$", "TOK_DOLLAR").replace(",", "TOK_COMMA")

    sql_insert = "'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'" % (
        convert_full_src_field, convert_full_des_field,
        convert_rel, convert_src_field,
        convert_des_field, src_table, des_table,
        update_time, sql_format, hive_lineage_log_id, ext)

    print(
        f"----------------------------\nrel={convert_rel} \n\nfull_src_field={convert_full_src_field} \n\nfull_des_field={convert_full_des_field}")
    execute_sql(DB_COR, DB_CONN,
                "INSERT INTO txkd_dc_hive_lineage_rel (full_src_field, full_des_field, rel, src_field, des_field, src_table, des_table, update_time, sql_format, hive_lineage_log_id, ext) VALUES (%s)" % sql_insert)


def read_from_table(DB_COR, lineage_id=246):
    sql_select = "SELECT lineage_str FROM developer.txkd_dc_hive_lineage_log where id=%s;" % lineage_id
    results = fetch_all(DB_COR,
                        sql_select)
    return results


def process_lineage_hook_info(lineage, DB_COR, DB_CONN):
    # clean_lineage = re.sub('[\s+]', '', lineage)
    clean_lineage = " ".join(lineage.split())
    # print(clean_lineage)
    # return

    data_dict = json.loads(clean_lineage)
    print("data_dict")
    print(data_dict)

    update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # _target_table = '_NULL'
    node_set = set()
    nodes_data = []
    links_data = []
    flag = True

    # 查询sql
    query_sql = data_dict["queryText"]

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
    i = 100
    j = 100
    edges = data_dict["edges"]
    for elem in edges:
        # print(elem)
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
            expression = base64.decodebytes(elem["expression"].encode()).decode('utf-8')
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

                    ## 打印点边关系
                    print(
                        f"{origin_column_name} -> {dest_column_name} ->@ {expression} << {origin_column_name.rsplit('.', 1)[0]} -> {dest_column_name.rsplit('.', 1)[0]} << {origin_column_name.rsplit('.', 1)[1]} -> {dest_column_name.rsplit('.', 1)[1]}")
                    print('-' * 160)
                    print(f"\t{query_sql}")
                    sql_format = sqlparse.format(query_sql, reindent=True, keyword_case='upper')
                    print(f"\t{sql_format}")

                    ## 写数据库
                    write_to_table(DB_COR, DB_CONN, origin_column_name, dest_column_name, expression,
                                   origin_column_name.rsplit('.', 1)[1], dest_column_name.rsplit('.', 1)[1],
                                   origin_column_name.rsplit('.', 1)[0], dest_column_name.rsplit('.', 1)[0],
                                   update_time, sql_format, id, '')


def process_txkd_dc_hive_lineage_info(lineage, hive_lineage_log_id, DB_COR, DB_CONN):
    clean_lineage = " ".join(lineage.split())

    data_dict = json.loads(clean_lineage)

    update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # # _target_table = '_NULL'
    # node_set = set()
    # nodes_data = []
    # links_data = []
    # flag = True

    # 查询sql
    query_sql = data_dict["queryText"]

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
            expression = base64.decodebytes(elem["expression"].encode()).decode('utf-8')
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

                    ## 打印点边关系
                    print(
                        f"{origin_column_name} -> {dest_column_name} ->@ {expression} << {origin_column_name.rsplit('.', 1)[0]} -> {dest_column_name.rsplit('.', 1)[0]} << {origin_column_name.rsplit('.', 1)[1]} -> {dest_column_name.rsplit('.', 1)[1]}")
                    print('-' * 160)
                    # print(f"\t{query_sql}")

                    sql_format = sqlparse.format(query_sql, reindent=True, keyword_case='upper')
                    sql_base64_encode = base64.encodebytes(sql_format.encode())
                    # print(f"{sql_base64_encode}")

                    origin_column_name = origin_column_name.replace("'", "TOK_SINGLE_QUOTE").replace("$",
                                                                                                 "TOK_DOLLAR").replace(
                        ",", "TOK_COMMA")
                    dest_column_name = dest_column_name.replace("'", "TOK_SINGLE_QUOTE").replace("$",
                                                                                             "TOK_DOLLAR").replace(
                        ",", "TOK_COMMA")
                    expression = expression.replace("'", "TOK_SINGLE_QUOTE").replace("$",
                                                                                 "TOK_DOLLAR").replace(
                        ",", "TOK_COMMA")
                    sql_format = str(sql_format).replace("'", "TOK_SINGLE_QUOTE").replace("$",
                                                                                      "TOK_DOLLAR").replace(
                        ",", "TOK_COMMA")

                    print(f"origin_column_name={origin_column_name}")
                    print(f"dest_column_name={dest_column_name}")
                    print(f"expression={expression}")

                    ## 写数据库
                    write_to_table(DB_COR, DB_CONN, origin_column_name, dest_column_name, expression,
                                   origin_column_name.rsplit('.', 1)[1], dest_column_name.rsplit('.', 1)[1],
                                   origin_column_name.rsplit('.', 1)[0], dest_column_name.rsplit('.', 1)[0],
                                   update_time, sql_format, hive_lineage_log_id, '')


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

    DB_COR = DB_CONN.cursor()

    # # 解析单条点边关系
    # lineage_id = 246
    # results = read_from_table(DB_COR, lineage_id)
    # lineage = results[0][0]
    # print(f"{lineage}")
    # print('-' * 160)
    # process_txkd_dc_hive_lineage_info(lineage, lineage_id, DB_COR, DB_CONN)

    ### 批量解析
    # for lineage_id in range(1, 23):
    for lineage_id in range(1, 2398):
        print(f"lineage_id={lineage_id}")

        results = read_from_table(DB_COR, lineage_id)
        lineage = results[0][0]
        # print(f"{lineage}")
        # print('-'*160)
        process_txkd_dc_hive_lineage_info(lineage, lineage_id, DB_COR, DB_CONN)

    sys.exit(0)


if __name__ == '__main__':
    main()
