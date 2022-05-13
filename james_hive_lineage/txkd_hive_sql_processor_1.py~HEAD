import datetime
import re
import datetime
import sys

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


## 清除注释
def clean_sql_comments(sql):
    sql_out = re.subn('\-\-.*?TOK_BACKSLASH_N', 'TOK_BACKSLASH_N', sql)[0]

    return sql_out

## 为date_sub()函数增加单引号
def add_quote_on_date(sql):
    rs = re.findall(r'''date_sub(\(\s*([0-9]{8})\s*\,)''', sql)
    if rs is not None:
        for t in rs:
            sql = sql.replace(t[0], t[0].replace(t[1], "TOK_SINGLE_QUOTE%sTOK_SINGLE_QUOTE" % t[1]))

    return sql

def read_from_table(DB_COR, id=1):
    sql_select = "SELECT sql_str FROM developer.txkd_dc_hive_sql where id=%s;" % id
    results = fetch_all(DB_COR,
                        sql_select)
    return results


def write_to_table(DB_COR, DB_CONN, sql_user, sql_db, sql_group, sql_str):
    ext = '{}'

    # """
    #     INSERT INTO txkd_dc_hive_sql (sql_str, update_time) VALUES ('', '');
    # """
    # sql_insert = "'%s', '%s'" % (sql_str, update_time)
    #
    # execute_sql(DB_COR, DB_CONN,
    #             "INSERT INTO txkd_dc_hive_sql (sql_str, update_time) VALUES (%s)" % sql_insert)

    """
        INSERT INTO txkd_dc_hive_sql_focus (username, dbname, groupname, sql_str) VALUES ('', '', '', '');
    """
    sql_insert = "'%s', '%s', '%s', '%s'" % (sql_user, sql_db, sql_group, sql_str)

    execute_sql(DB_COR, DB_CONN,
                "INSERT INTO txkd_dc_hive_sql_focus (username, dbname, groupname, sql_str) VALUES (%s)" % sql_insert)


def process_sql(sql_file):
    update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file = open(sql_file, 'r')

    cnt = 10000
    errCnt = 0
    ## readlines()
    try:
        lines = file.readlines()
        for line in lines:
            if cnt > 0:
                cnt -= 1
                print('-' * 160)
                print(line)
                line = clean_sql_comments(line)
                print(line)
                try:
                    (sql_user, sql_db, sql_group, sql_str) = line.split("；")
                    sql_str = add_quote_on_date(sql_str)
                    write_to_table(DB_COR, DB_CONN, sql_user, sql_db, sql_group, " ".join(sql_str.split()))
                    # print(f"sql_user={sql_user}, sql_db={sql_db}, sql_group={sql_group}")
                    # print(" ".join(sql_str.split()).replace('HEIHEIHEIAABBCC', 'TOK_BACKSLASH_N'))
                except ValueError as err:
                    errCnt += 1
                    print(f">>> {line}")

    finally:
        file.close()

    # print(f"cnt={cnt}")
    # print(f"errCnt={errCnt}")

    # ## readline()
    # cnt = 10
    #
    # try:
    #     while cnt > 0:
    #         cnt -= 1
    #         line = file.readline()
    #         if line:
    #             re.sub('[\s+]', ' ', line)
    #             sql_str = re.sub("\\'", 'SINGLE_QUOTE', " ".join(line.split()))
    #             print(">>> " + sql_str)
    #             write_to_table(DB_COR, DB_CONN, sql_str, update_time)
    #         else:
    #             break
    # finally:
    #     file.close()


def convert_tdw_sql_to_hive_sql(sql):
    if not sql:
        return None


def main():
    sql_file = './_data/txkd_dc_sql_300s.sql'
    process_sql(sql_file)

    # id = 1
    # results = read_from_table(DB_COR, id)
    # record = results[0][0]
    # print(f"{record}")
    # print('-' * 160)


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

    sys.exit(0)
