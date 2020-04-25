# -*- coding: utf-8 -*-
import datetime
import inspect

import pandas as pd
import pymysql
import json
import os
import sys

from sqlalchemy import create_engine

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
sys.path.insert(0, '../utils')

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)


# reload(sys)
# sys.setdefaultencoding("utf-8")

def fetch_all(COR, sql):  # wrapper for sql
    COR.execute(sql)
    return COR.fetchall()


def execute_sql(COR, CON, sql):
    COR.execute(sql)
    CON.commit()


def fetch_yqc_spider_results():
    print("fetch_yqc_spider_results()...")

    # [YQC_SPIDER_DB]
    db_host = 'localhost'
    db_user = 'developer'
    db_passwd = 'developer'
    db_db = 'developer'
    db_port = int(3306)
    sql_select = """
SELECT *
FROM
  (SELECT t_cont.*
   FROM
     (SELECT min(id) id,
             title
      FROM developer.yqc_spider
      GROUP BY title) t_id
   LEFT JOIN
     (SELECT id,
             title,
             url,
             pub_time,
             pub_org,
             doc_id,
             index_id,
             key_cnt,
             region,
             update_time
      FROM developer.yqc_spider
      WHERE update_time>'2020-04-24 00:00:00') t_cont ON t_id.id=t_cont.id) tt
WHERE title IS NOT NULL
ORDER BY region,
         key_cnt DESC;
         """

    engine = create_engine("mysql+pymysql://%s:%s@%s:%s/%s" % (db_user, db_passwd, db_host, db_port, db_db))

    df = pd.read_sql_query(sql_select, engine)
    df = df.applymap(lambda x: str(x).strip())

    print(df)
    os_info = os.uname()
    if os_info.sysname == 'Darwin':
        csv_file_path = r"/Users/qjiang/Desktop/_CURRNET_WORK/_爬虫/yqc_spider_20200425.csv"
    else:
        csv_file_path = r"/home/james/桌面/_CURRENT_WORK/_爬虫数据/yqc_spider_20200425.csv"
    df.to_csv(csv_file_path)
    print("Results has been saved.")

    # YQC_DB_CONN = pymysql.connect(host=db_host, user=db_user, passwd=db_passwd,
    #                               db=db_db,
    #                               port=db_port,
    #                               charset='utf8')
    #
    # YQC_DB_CONN = YQC_DB_CONN.cursor()
    #
    # results = fetch_all(YQC_DB_CONN,
    #                     sql_select)
    # results = list(results)
    #
    # for record in results:
    #     print(str(list(record).__sizeof__()) + str(record))
    # print(str(list(record).__) + str(record))


def main():
    fetch_yqc_spider_results()


if __name__ == '__main__':
    main()
