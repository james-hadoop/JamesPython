import psycopg2
import pymysql

from py_kd_data_common_proj.ds_utils.ds_pymysql_util import fetch_all

pg_conn = psycopg2.connect(database="zcsd", user="developer", password="developer", host="localhost", port="5432")
pg_cur = pg_conn.cursor()

my_conn = pymysql.connect(host="localhost", user="developer", passwd="developer",
                          db="developer",
                          port=3306,
                          charset='utf8')

my_cur = my_conn.cursor()

pg_cur.execute("SELECT * from app.sys_user")
pg_rows = pg_cur.fetchall()
for r in pg_rows:
    print(r)

print('-' * 160)
my_cur.execute("select * from t_ds_demo")
my_rows = my_cur.fetchall()
for r in my_rows:
    print(r)

pg_conn.close()
my_conn.close()
