# 1. 使用ds_assets/DDL_t_ds_demo.sql文件创建本地数据表
# 2. 获取配置参数文件ds_conf/config.conf中指定的库表信息
# 3. 使用pymysql写入和读取MySQL数据库中的信息

import datetime
import os

import configobj
import pymysql

from ds_utils.ds_pymysql_util import execute_sql, fetch_all

config_path = os.getcwd() + '/../ds_conf/config.conf'
CO = configobj.ConfigObj(config_path)


def write_to_table(DB_COR, DB_CONN):
    update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    update_name = 'jamesqjiang'
    value = 'i am a value@' + update_time
    ext = '{}'

    sql_insert = "'%s', '%s', '%s', '%s'" % (
        update_time, update_name, value, ext)

    execute_sql(DB_COR, DB_CONN,
                "insert into t_ds_demo (update_time, update_name, value, ext) values (%s)" % sql_insert)


def read_from_table(DB_COR):
    sql_select = "select * from t_ds_demo where update_time;"
    results = fetch_all(DB_COR,
                        sql_select)
    return results


def main():
    LOCAL_DB = CO['LOCAL_DB']
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

    # 写入一条数据
    write_to_table(DB_COR, DB_CONN)

    # 读出所有数据
    results = read_from_table(DB_COR)
    """
        (
            (1, datetime.datetime(2020, 4, 1, 12, 6, 41), 'jamesqjiang', 'i am a value@2020-04-01 12:06:41', '{}'),
            (2, datetime.datetime(2020, 4, 1, 14, 12, 48), 'jamesqjiang', 'i am a value@2020-04-01 14:12:48', '{}')
        )
    """
    print(results)


if __name__ == '__main__':
    main()
