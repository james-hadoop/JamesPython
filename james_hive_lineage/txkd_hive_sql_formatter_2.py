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

import requests
import simplejson
import sqlparse
from py_kd_data_common_proj.ds_utils.ds_pymysql_util import fetch_all, execute_sql


def read_from_table(DB_COR):
    sql_select = "SELECT sql_str, dbname FROM developer.txkd_dc_hive_sql_focus_all limit 2"
    sql_select = "SELECT sql_str, dbname FROM developer.txkd_dc_hive_sql_focus_all"
    results = fetch_all(DB_COR,
                        sql_select)
    return results


def write_to_table(DB_COR, DB_CONN, sql_str, is_valid):
    """
        INSERT INTO txkd_dc_hive_sql_validate (sql_str, is_valid) VALUES ('', '');
    """
    sql_insert = "'%s', '%s'" % (sql_str, is_valid)

    execute_sql(DB_COR, DB_CONN,
                "INSERT INTO txkd_dc_hive_sql_validate (sql_str, is_valid) VALUES (%s, %d)" % sql_insert)


# 为date_sub()函数增加单引号
def add_quote_on_date_for_DATE_SUB(sql):
    rs = re.findall(r'''date_sub(\(\s*([0-9]{8})\s*\,)''', sql)
    if rs is not None:
        for t in rs:
            sql = sql.replace(t[0], t[0].replace(t[1], "TOK_SINGLE_QUOTE%sTOK_SINGLE_QUOTE" % t[1]))
    return sql


# 为date_add()函数增加单引号
def add_quote_on_date_for_DATE_ADD(sql):
    rs = re.findall(r'''date_add(\(\s*([0-9]{8})\s*\,)''', sql)
    if rs is not None:
        for t in rs:
            sql = sql.replace(t[0], t[0].replace(t[1], "TOK_SINGLE_QUOTE%sTOK_SINGLE_QUOTE" % t[1]))
    return sql


# 常量替换
def mysql2sql(sql):
    return sql.replace("TOK_SINGLE_QUOTE", "'").replace("TOK_BACKSLASH_N", " ").replace("INSERT TABLE",
                                                                                        "INSERT INTO").replace("TYPE",
                                                                                                               "`type`").replace(
        "interval", "`interval`").replace("INSERT OVERWRITE INTO TABLE", "INSERT INTO").replace("INSERT INTO TABLE",
                                                                                                "INSERT INTO").replace(
        ") GROUP BY", ") t_alias_tt GROUP BY")


def sql2mysql(sql):
    return sql.replace("'", "TOK_SINGLE_QUOTE").replace("\n", "TOK_BACKSLASH_N")


# 为join缺少的别名加上别名
def solve_less_alias_problem(sql):
    rs = re.findall(r'''(\)\)\s{1,5}(\w{1,20}))\s{1,5}ON''', sql)
    if rs is not None:
        for t in rs:
            sql = sql.replace(t[0], ') t_alias_tt) ' + t[1])
    return sql


# 删除partion子句
def remove_partition_part(sql):
    sql = re.sub(r"(?i)(partition\s*\(\s*\w*\s*=\s*\w*\s*\))", " ", sql)

    return sql


# 删除overwrite子句
def remove_overwrite_table(sql):
    sql = re.sub(r"""(?i)OVERWRITE\s*[INTO]*\s*TABLE""", " INTO ", sql)

    return sql


def validate_sql():
    results = read_from_table(DB_COR)

    sql_list = [[item[0], item[1]] for item in results]

    with open("/Users/qjiang/workspace4py/JamesPython/james_hive_lineage/_log/txkd_dc_sql_60_big.sql",
              "a+") as f:
        for s in sql_list:
            db = s[1]
            sql = str(s[0]).replace("TOK_SINGLE_QUOTE", "'").replace("TOK_BACKSLASH_N", " ").replace("::", ".").replace(
                "INSERT OVERWRITE TABLE", "INSERT INTO").replace("INSERT TABLE", "INSERT INTO")
            sql = sql + ";"
            sql = sqlparse.format(sql, reindent=True, keyword_case='upper')
            sql = " ".join(sql.split())
            sql = solve_less_alias_problem(sql)
            sql = add_quote_on_date_for_DATE_ADD(sql)
            sql = add_quote_on_date_for_DATE_SUB(sql)
            sql = remove_partition_part(sql)
            sql = remove_overwrite_table(sql)

            sql = mysql2sql(sql)
            f.write("use " + db + ";" + sql + "\n")
            # f.write(db + "；" + sql + "\n")


def main():
    validate_sql()
    # code = """
    # INSERT INTO sng_mp_etldata.dwa_cc_kd_pop_filter_pv_uv_daily  select f_date, type, pop_cnt, pv_d, pv_m, uv_d, uv_m, total_uv  from  (select p.pop_date f_date, '图文' type, pop_cnt, pv_d, pv_m, uv_d, uv_m, total_uv  from  (select pop_date,  count(distinct rowkey) pop_cnt,   sum(pv_d) pv_d,   sum(pv_m) pv_m  from  (select 20200630 pop_date, a.rowkey rowkey, pv_d, pv_m  from  (select rowkey  from pcg_txkd_shared_data_app.t_dim_fcc_b_article_rowkey_acc_d  where p_date = 20200630  and ((metrics_pop_fst_filter = 1 and from_unixtime(cast(substr(timestamp_pop_fst_end,1,10)as bigint),'yyyyMMdd') = 20200630)   or (metrics_pop_sec_filter = 1 and from_unixtime(cast(substr(timestamp_pop_sec_end,1,10)as bigint),'yyyyMMdd') = 20200630))  and st_kd = 0  and metrics_asn_human_pass = 1   and content_type = '图文'  ) a  left join  (select rowkey,   sum(case when p_date=20200630 then total_pv else 0 end) pv_d,  sum(total_pv) pv_m  from pcg_txkd_shared_data_app.t_dwt_consume_article_rowkeyperformance_normal_d  where p_date between date_sub('20200630',29) and 20200630  and sp_app_id = 'kd'  group by rowkey  ) b   on a.rowkey = b.rowkey  ) n   group by pop_date  ) p  left join    (select 20200630 pop_date, uv_d, uv_m, total_uv  from   (select count(distinct case when ptime = 20200630 then user_id end) total_uv,   count(distinct case when is_low = 1 and ptime = 20200630 then user_id end) uv_d,  count(distinct case when is_low = 1 then user_id end) uv_m  from  (select rowkey,   case when metrics_asn_human_pass = 1   and ((metrics_pop_fst_filter = 1 and from_unixtime(cast(substr(timestamp_pop_fst_end,1,10)as bigint),'yyyyMMdd') = 20200630)   or (metrics_pop_sec_filter = 1 and from_unixtime(cast(substr(timestamp_pop_sec_end,1,10)as bigint),'yyyyMMdd') = 20200630))  and st_kd = 0  then 1 else 0 end as is_low  from pcg_txkd_shared_data_app.t_dim_fcc_b_article_rowkey_acc_d  where p_date = 20200630   and content_type = '图文'  ) s  join  (select substr(p_date,1,8) ptime, rowkey, user_id  from pcg_txkd_shared_data_app.t_ods_consume_kd_basic_detail_h  where substr(p_date,1,8) between date_sub('20200630', 29) and 20200630  and action_type = 'exposure'   and scene = 'detail_page'   and length(rowkey) = 16  ) t   on s.rowkey = t.rowkey  )  ) q  on p.pop_date = q.pop_date   union all    select p.pop_date f_date, '视频' type, pop_cnt, pv_d, pv_m, uv_d, uv_m, total_uv  from  (select pop_date,  count(distinct rowkey) pop_cnt,   sum(pv_d) pv_d,   sum(pv_m) pv_m  from  (select 20200630 pop_date, a.rowkey rowkey, pv_d, pv_m  from  (select rowkey  from pcg_txkd_shared_data_app.t_dim_fcc_b_video_rowkey_acc_d  where p_date = 20200630  and metrics_asn_human_pass = 1   and ((metrics_pop_fst_filter = 1 and from_unixtime(cast(substr(timestamp_pop_fst_end,1,10)as bigint),'yyyyMMdd') = 20200630)   or (metrics_pop_sec_filter = 1 and from_unixtime(cast(substr(timestamp_pop_sec_end,1,10)as bigint),'yyyyMMdd') = 20200630))  and st_kd = 0  and content_type in ('短视频','小视频')  ) a  left join  (select rowkey,   sum(case when p_date=20200630 then total_vv else 0 end) pv_d,  sum(total_vv) pv_m  from pcg_txkd_shared_data_app.t_dwt_consume_video_rowkeyperformance_normal_d  where p_date between date_sub('20200630',29) and 20200630  and sp_app_id = 'kd'  group by rowkey  ) b   on a.rowkey = b.rowkey  ) n   group by pop_date  ) p  left join    (select 20200630 pop_date, uv_d, uv_m, total_uv  from   (select count(distinct case when ptime = 20200630 then user_id end) total_uv,   count(distinct case when is_low = 1 and ptime = 20200630 then user_id end) uv_d,  count(distinct case when is_low = 1 then user_id end) uv_m  from  (select rowkey,   case when metrics_asn_human_pass = 1   and ((metrics_pop_fst_filter = 1 and from_unixtime(cast(substr(timestamp_pop_fst_end,1,10)as bigint),'yyyyMMdd') = 20200630)   or (metrics_pop_sec_filter = 1 and from_unixtime(cast(substr(timestamp_pop_sec_end,1,10)as bigint),'yyyyMMdd') = 20200630))  and st_kd = 0  then 1 else 0 end as is_low  from pcg_txkd_shared_data_app.t_dim_fcc_b_video_rowkey_acc_d  where p_date = 20200630   and content_type in ('短视频','小视频')  ) s  join  (select substr(p_date,1,8) ptime, rowkey, user_id  from pcg_txkd_shared_data_app.t_ods_consume_kd_basic_detail_h  where substr(p_date,1,8) between date_sub('20200630', 29) and 20200630  and action_type = 'play'   and scene in ('feeds', 'float_layer')   and length(rowkey) = 16  ) t   on s.rowkey = t.rowkey  )  ) q  on p.pop_date = q.pop_date  ) t
    # """
    # print(f"code={code}")
    #
    # sql_format = sqlparse.format(code, reindent=True, keyword_case='upper')
    # print(" ".join(sql_format.split()))

    # operate = "compress_dfdfdfd"
    #
    # data = {'code': code,
    #         'operate': operate}
    #
    # r = requests.post('https://tool.lu/sql/ajax.html', json={'code': code,
    #                                                          'operate': operate})
    # ret_code = r.status_code
    # print(f"ret_code={ret_code}")
    # print(r.json())
    # print(r.content)

    pass


if __name__ == '__main__':
    # 配置信息
    config_path = os.getcwd() + '/../james_config/james_config.conf'
    CO = configobj.ConfigObj(config_path)

    # 数据库连接信息
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

    # 执行逻辑
    main()

    # 退出
    sys.exit(0)
