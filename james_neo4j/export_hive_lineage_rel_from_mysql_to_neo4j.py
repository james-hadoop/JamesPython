import sys

from neo4j import GraphDatabase
import datetime

import configobj
import pymysql
import json
import os
import re
import base64

from james_neo4j.james_neo4j_demo_create import Neo4jHandler

from py_kd_data_common_proj.ds_utils.ds_pymysql_util import fetch_all, execute_sql

config_path = os.getcwd() + '/../james_config/james_config.conf'
CO = configobj.ConfigObj(config_path)


def read_from_table(DB_COR, id):
    sql_select = "SELECT full_src_field, src_field, src_table, full_des_field, des_field, des_table, rel FROM developer.hive_lineage_rel"

    if id:
        sql_select = sql_select + " where id = % s;" % id
    # print(f"sql_select={sql_select}")

    sql_results = fetch_all(DB_COR,
                            sql_select)
    return sql_results


if __name__ == "__main__":
    print("export_hive_lineage_rel_from_mysql_to_neo4j start...")

    uri = "bolt://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("james", "james"))
    MyNH = Neo4jHandler(driver)

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

    results = read_from_table(DB_COR, None)
    rels = [
        'CREATE (src:Field {full_src_field:"%s",src_field:"%s",src_table:"%s"}),(des:Field {full_des_field:"%s",des_field:"%s",des_table:"%s"}),(src)-[:%s]->(des)' % (
            rel[0], rel[1], rel[2], rel[3], rel[4], rel[5], "转换") for rel in
        results]
    for rel in rels:
        print(rel)
        cypher_exec = rel
        MyNH.cypherexecuter(cypher_exec)

    print("export_hive_lineage_rel_from_mysql_to_neo4j stop...")
    sys.exit(0)
