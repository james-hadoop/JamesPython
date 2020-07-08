import datetime
import re
import datetime

import configobj
import pymysql
import json
import os
import re
import base64

import sqlparse
from py_kd_data_common_proj.ds_utils.ds_pymysql_util import fetch_all, execute_sql

config_path = os.getcwd() + '/../james_config/james_config.conf'
CO = configobj.ConfigObj(config_path)


def read_from_table(DB_COR, id=1):
    sql_select = "SELECT sql_str FROM developer.txkd_dc_hive_sql where id=%s;" % id
    results = fetch_all(DB_COR,
                        sql_select)
    return results


def write_to_table(DB_COR, DB_CONN, sql_str,
                   update_time):
    ext = '{}'

    """
        INSERT INTO txkd_dc_hive_sql (sql_str, update_time) VALUES ('', '');
    """
    sql_insert = "'%s', '%s'" % (sql_str, update_time)

    execute_sql(DB_COR, DB_CONN,
                "INSERT INTO txkd_dc_hive_sql (sql_str, update_time) VALUES (%s)" % sql_insert)


def export_sql_to_mysql(sql_file):
    update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file = open(sql_file, 'r')

    # ## readlines()
    # try:
    #     lines = file.readlines()
    #     print(type(lines), lines)
    #     for line in lines:
    #         print(line)
    # finally:
    #     file.close()

    ## readline()
    cnt = 10

    try:
        while cnt > 0:
            cnt -= 1
            line = file.readline()
            if line:
                re.sub('[\s+]', ' ', line)
                sql_str = re.sub("\\'", 'SINGLE_QUOTE', " ".join(line.split()))
                print(">>> " + sql_str)
                write_to_table(DB_COR, DB_CONN, sql_str, update_time)
            else:
                break
    finally:
        file.close()


def convert_tdw_sql_to_hive_sql(sql):
    if not sql:
        return None


def main():
    sql_file = './_data/insert_select.sql'
    # export_sql_to_mysql(sql_file)

    id = 1
    results = read_from_table(DB_COR, id)
    record = results[0][0]
    print(f"{record}")
    print('-' * 160)


if __name__ == '__main__':
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

    main()
