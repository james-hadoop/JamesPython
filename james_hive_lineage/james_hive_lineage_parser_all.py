# coding:utf-8
import datetime

import configobj
import pymysql
import json
import os
import re
import base64
import sys

from pyecharts import options as opts
from pyecharts.charts import Graph

from py_kd_data_common_proj.ds_utils.ds_pymysql_util import fetch_all, execute_sql

config_path = os.getcwd() + '/../james_config/james_config.conf'
CO = configobj.ConfigObj(config_path)


def write_to_table(DB_COR, DB_CONN, full_src_field, full_des_field, rel, src_field, des_field, src_table, des_table,
                   update_time, ext):
    update_name = 'jamesqjiang'
    value = 'i am a value@' + update_time
    ext = '{}'

    """
        INSERT INTO hive_lineage_rel (full_src_field, full_des_field, rel, src_field, des_field, src_table, des_table, update_time, ext) VALUES ('', '', '', '', '', '', '', '', '');

    """
    sql_insert = "'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'" % (
        full_src_field, full_des_field, re.sub("\\'", 'SINGLE_QUOTE', rel), src_field, des_field, src_table, des_table,
        update_time, ext)

    execute_sql(DB_COR, DB_CONN,
                "INSERT INTO hive_lineage_rel (full_src_field, full_des_field, rel, src_field, des_field, src_table, des_table, update_time, ext) VALUES (%s)" % sql_insert)


def read_from_table(DB_COR, lineage_id=14):
    sql_select = "SELECT lineage_str FROM developer.hive_lineage_log where id=%s;" % lineage_id
    results = fetch_all(DB_COR,
                        sql_select)
    return results


def process_lineage_hook_info(lineage, DB_COR, DB_CONN):
    clean_lineage = re.sub('[\s+]', '', lineage)
    # print(clean_lineage)
    # return

    data_dict = json.loads(clean_lineage)

    update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # _target_table = '_NULL'
    node_set = set()
    nodes_data = []
    links_data = []
    flag = True

    # 所有顶点装入字典
    vertices = data_dict["vertices"]
    vertices_dict = {}
    for elem in vertices:
        key = elem["id"]
        type = elem["vertexType"]
        value = elem["vertexId"]
        vertices_dict[key] = (type, value)

    vertices_dict[-99] = ('_USER_DEFINE', "_USER_DEFINE")

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

        ## todo
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
                        origin_column_name = "_USER_DEFINE._USER_DEFINE._USER_DEFINE"
                    if vertices_dict[source][0] == "COLUMN":
                        origin_column_name = vertices_dict[source][1]
                    elif vertices_dict[source][0] == "TABLE":
                        origin_column_name = vertices_dict[source][1] + "." + expression

                    ## 打印点边关系
                    print(
                        f"{origin_column_name} -> {dest_column_name} ->@ {expression} << {origin_column_name.rsplit('.', 1)[0]} -> {dest_column_name.rsplit('.', 1)[0]} << {origin_column_name.rsplit('.', 1)[1]} -> {dest_column_name.rsplit('.', 1)[1]}")

                    # ## 写数据库
                    # write_to_table(DB_COR, DB_CONN, origin_column_name, dest_column_name, expression,
                    #                origin_column_name.rsplit('.', 1)[1], dest_column_name.rsplit('.', 1)[1],
                    #                origin_column_name.rsplit('.', 1)[0], dest_column_name.rsplit('.', 1)[0],
                    #                update_time, '')


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

    lineage_id = 100
    results = read_from_table(DB_COR, lineage_id)
    lineage = results[0][0]
    print(f"{lineage}")
    print('-'*160)
    process_lineage_hook_info(lineage, DB_COR, DB_CONN)

    # ### 批量解析
    # # for lineage_id in range(14, 23):
    # for lineage_id in range(14, 22):
    #     print(f"lineage_id={lineage_id}")
    #
    #     results = read_from_table(DB_COR, lineage_id)
    #     lineage = results[0][0]
    #     # print(f"{lineage}")
    #     # print('-'*160)
    #     process_lineage_hook_info(lineage, DB_COR, DB_CONN)




if __name__ == '__main__':
    main()

    sys.exit(0)
