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


# 为date_sub()函数中的日期增加单引号
def add_quote_on_date_for_DATE_SUB(sql):
    rs = re.findall(r'''date_sub(\(\s*([0-9]{8})\s*\,)''', sql)
    if rs is not None:
        for t in rs:
            sql = sql.replace(t[0], t[0].replace(t[1], "TOK_SINGLE_QUOTE%sTOK_SINGLE_QUOTE" % t[1]))
    return sql


# 为date_add()函数中的日期增加单引号
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


def main():
    # sql = """
    # INSERT INTO sng_mp_etldata.dwa_cc_kb_pop_with_huilao_pv_uv_daily SELECT f_date, TYPE, pop_cnt, pv_d, pv_m, uv_d, uv_m, total_uv FROM (SELECT p.pop_date f_date, '图文' TYPE, pop_cnt, pv_d, pv_m, uv_d, uv_m, total_uv FROM (SELECT pop_date, count(DISTINCT rowkey) pop_cnt, sum(pv_d) pv_d, sum(pv_m) pv_m FROM (SELECT 20200630 pop_date, a.rowkey rowkey, pv_d, pv_m FROM (SELECT rowkey FROM pcg_txkd_shared_data_app.t_dim_fcc_b_article_rowkey_acc_d WHERE p_date = 20200630 AND ((metrics_pop_fst_filter = 1 AND from_unixtime(cast(substr(timestamp_pop_fst_end, 1, 10)AS bigint), 'yyyyMMdd') = 20200630) OR (metrics_pop_sec_filter = 1 AND from_unixtime(cast(substr(timestamp_pop_sec_end, 1, 10)AS bigint), 'yyyyMMdd') = 20200630)) AND st_kd = 0 AND (metrics_asn_human_pass = 1 OR send_audit_type = '4') AND content_type = '图文' ) a LEFT JOIN (SELECT rowkey, sum(CASE WHEN p_date=20200630 THEN total_pv ELSE 0 END) pv_d, sum(total_pv) pv_m FROM pcg_txkd_shared_data_app.t_dwt_consume_article_rowkeyperformance_normal_d WHERE p_date BETWEEN date_sub('20200630', 29) AND 20200630 AND sp_app_id = 'kb' GROUP BY rowkey) b ON a.rowkey = b.rowkey) n GROUP BY pop_date) p LEFT JOIN (SELECT 20200630 pop_date, uv_d, uv_m, total_uv FROM (SELECT count(DISTINCT CASE WHEN ptime = 20200630 THEN user_id END) total_uv, count(DISTINCT CASE WHEN is_low = 1 AND ptime = 20200630 THEN user_id END) uv_d, count(DISTINCT CASE WHEN is_low = 1 THEN user_id END) uv_m FROM (SELECT rowkey, CASE WHEN (metrics_asn_human_pass = 1 OR send_audit_type = '4') AND ((metrics_pop_fst_filter = 1 AND from_unixtime(cast(substr(timestamp_pop_fst_end, 1, 10)AS bigint), 'yyyyMMdd') = 20200630) OR (metrics_pop_sec_filter = 1 AND from_unixtime(cast(substr(timestamp_pop_sec_end, 1, 10)AS bigint), 'yyyyMMdd') = 20200630)) AND st_kd = 0 THEN 1 ELSE 0 END AS is_low FROM pcg_txkd_shared_data_app.t_dim_fcc_b_article_rowkey_acc_d WHERE p_date = 20200630 AND content_type = '图文' ) s JOIN (SELECT substr(p_date, 1, 8) ptime, rowkey, user_id FROM pcg_txkd_shared_data_app.t_ods_consume_kb_basic_detail_h WHERE substr(p_date, 1, 8) BETWEEN date_sub('20200630', 29) AND 20200630 AND action_type = 'click' AND length(rowkey) = 16 ) t ON s.rowkey = t.rowkey JOIN (SELECT omgid FROM omg_mobile_newsdev.kuaibao_dw_antispam_active_user_list WHERE imp_date = 20200630 ) p ON t.user_id = p.omgid)) q ON p.pop_date = q.pop_date UNION ALL SELECT p.pop_date f_date, '视频' TYPE, pop_cnt, pv_d, pv_m, uv_d, uv_m, total_uv FROM (SELECT pop_date, count(DISTINCT rowkey) pop_cnt, sum(pv_d) pv_d, sum(pv_m) pv_m FROM (SELECT 20200630 pop_date, a.rowkey rowkey, pv_d, pv_m FROM (SELECT rowkey FROM pcg_txkd_shared_data_app.t_dim_fcc_b_video_rowkey_acc_d WHERE p_date = 20200630 AND ((metrics_pop_fst_filter = 1 AND from_unixtime(cast(substr(timestamp_pop_fst_end, 1, 10)AS bigint), 'yyyyMMdd') = 20200630) OR (metrics_pop_sec_filter = 1 AND from_unixtime(cast(substr(timestamp_pop_sec_end, 1, 10)AS bigint), 'yyyyMMdd') = 20200630)) AND st_kd = 0 AND (metrics_asn_human_pass = 1 OR send_audit_type = '4') AND content_type IN ('短视频', '小视频') ) a LEFT JOIN (SELECT rowkey, sum(CASE WHEN p_date=20200630 THEN total_vv ELSE 0 END) pv_d, sum(total_vv) pv_m FROM pcg_txkd_shared_data_app.t_dwt_consume_video_rowkeyperformance_normal_d WHERE p_date BETWEEN date_sub('20200630', 29) AND 20200630 AND sp_app_id = 'kb' GROUP BY rowkey) b ON a.rowkey = b.rowkey) n GROUP BY pop_date) p LEFT JOIN (SELECT 20200630 pop_date, uv_d, uv_m, total_uv FROM (SELECT count(DISTINCT CASE WHEN ptime = 20200630 THEN user_id END) total_uv, count(DISTINCT CASE WHEN is_low = 1 AND ptime = 20200630 THEN user_id END) uv_d, count(DISTINCT CASE WHEN is_low = 1 THEN user_id END) uv_m FROM (SELECT rowkey, CASE WHEN (metrics_asn_human_pass = 1 OR send_audit_type = '4') AND ((metrics_pop_fst_filter = 1 AND from_unixtime(cast(substr(timestamp_pop_fst_end, 1, 10)AS bigint), 'yyyyMMdd') = 20200630) OR (metrics_pop_sec_filter = 1 AND from_unixtime(cast(substr(timestamp_pop_sec_end, 1, 10)AS bigint), 'yyyyMMdd') = 20200630)) AND st_kd = 0 THEN 1 ELSE 0 END AS is_low FROM pcg_txkd_shared_data_app.t_dim_fcc_b_video_rowkey_acc_d WHERE p_date = 20200630 AND content_type IN ('短视频', '小视频') ) s JOIN (SELECT substr(p_date, 1, 8) ptime, rowkey, user_id FROM pcg_txkd_shared_data_app.t_ods_consume_kb_basic_detail_h WHERE substr(p_date, 1, 8) BETWEEN date_sub('20200630', 29) AND 20200630 AND action_type = 'play' AND scene IN ('feeds', 'float_layer') AND length(rowkey) = 16 ) t ON s.rowkey = t.rowkey JOIN (SELECT omgid FROM omg_mobile_newsdev.kuaibao_dw_antispam_active_user_list WHERE imp_date = 20200630 ) p ON t.user_id = p.omgid)) q ON p.pop_date = q.pop_date) t;
    #
    # """

    #     sql = """
    #     INSERT overwrite  into TABLE mattyu_dw_comment_new partition(dt=20200630) SELECT 20200630, uin, op_type, nvl(source_type, '未知'), sum(first_quote) first_quote, sum(second_quote) second_quote, sum(total_quote) total_quote FROM (SELECT uin, op_type, source_type, if(comment_level IS NULL, op_cnt, 0) AS first_quote, if(comment_level IS NULL, cast((if(length(sub_arr)>0, size(split(sub_arr, ',')), 0) * op_cnt) AS bigint), op_cnt) AS second_quote, cast((if(length(sub_arr)>0, size(split(sub_arr, ',')), 0) + 1) * op_cnt AS bigint) AS total_quote FROM (SELECT uin, op_type, 1 AS op_cnt, get_json_object(get_json_object(extra_info, '$.r5'), '$.entry') AS source_type, get_json_object(get_json_object(extra_info, '$.r5'), '$.sub_comment_id') AS comment_level, regexp_replace(get_json_object(get_json_object(extra_info, '$.r5'), '$.show_sub_comment_id'), '[^0-9,]', '') sub_arr FROM sng_mp_etldata.t_mp_article_click_table_hourly WHERE tdbank_imp_date BETWEEN 2020063000 AND 2020063023 AND op_type = '0X8009992') UNION ALL SELECT uin, op_type, source_type, if(comment_level IS NULL, op_cnt, 0) AS first_quote, if(comment_level IS NULL, cast((if(length(sub_arr)>0, size(split(sub_arr, ',')), 0) * op_cnt) AS bigint), op_cnt) AS second_quote, cast((if(length(sub_arr)>0, size(split(sub_arr, ',')), 0) + 1) * op_cnt AS bigint) AS total_quote FROM (SELECT uin, op_type, op_cnt, get_json_object(d4, '$.entry') AS source_type, get_json_object(d4, '$.sub_comment_id') AS comment_level, regexp_replace(get_json_object(d4, '$.show_sub_comment_id'), '[^0-9,]', '') sub_arr FROM hlw.t_dw_dc01160 WHERE tdbank_imp_date BETWEEN 2020063000 AND 2020063023 AND op_type = '0X8009992' AND op_cnt<10) UNION ALL SELECT uin, op_type, get_json_object(d4, '$.content_type') AS source_type, if(d1=='1', op_cnt, 0) AS first_quote, if(d1 IN ('2', '3'),op_cnt, 0) AS second_quote, op_cnt AS total_quote FROM hlw.t_dw_dc01160 WHERE tdbank_imp_date BETWEEN 2020063000 AND 2020063023 AND op_type='0X8009208' AND op_cnt<10 UNION ALL SELECT uin, op_type, get_json_object(get_json_object(extra_info, '$.r5'), '$.entry') AS source_type, 0 AS first_quote, 0 AS second_quote, get_json_object(get_json_object(extra_info, '$.r5'), '$.read_time') AS quote FROM sng_mp_etldata.t_mp_article_click_table_hourly WHERE tdbank_imp_date BETWEEN 2020063000 AND 2020063023 AND op_type='0X8009991' AND get_json_object(get_json_object(extra_info, '$.r5'), '$.read_time') BETWEEN 2000 AND 600000 UNION ALL SELECT uin, op_type, get_json_object(d4, '$.entry') AS source_type, 0 AS first_quote, 0 AS second_quote, get_json_object(d4, '$.read_time') AS quote FROM hlw.t_dw_dc01160 WHERE tdbank_imp_date BETWEEN 2020063000 AND 2020063023 AND op_type='0X8009991' AND get_json_object(d4, '$.read_time') BETWEEN 2000 AND 600000 UNION ALL SELECT uin, op_type, get_json_object(d4, '$.content_type') AS source_type, if(d1='1', op_cnt, 0) AS first_quote, if(d1 IN ('2', '3'),op_cnt, 0) AS second_quote, op_cnt AS total_quote FROM hlw.t_dw_dc01160 WHERE tdbank_imp_date BETWEEN 2020063000 AND 2020063023 AND op_type='0X800920A' AND op_cnt<10 UNION ALL SELECT uin, op_type, get_json_object(get_json_object(extra_info, '$.r5'), '$.entry') AS source_type, if(get_json_object(get_json_object(extra_info, '$.r5'), '$.comment_level')='0', 1, 0) AS first_quote, if(get_json_object(get_json_object(extra_info, '$.r5'), '$.comment_level') IN ('1', '2'),1, 0) AS second_quote, 1 AS total_quote FROM sng_mp_etldata.t_mp_article_click_table_hourly WHERE tdbank_imp_date BETWEEN 2020063000 AND 2020063023 AND op_type='0X8009669' AND get_json_object(get_json_object(extra_info, '$.r5'), '$.actionsheet_choose')='1' UNION ALL SELECT uin, op_type, get_json_object(d4, '$.entry') AS source_type, if(get_json_object(d4, '$.comment_level')='0', op_cnt, 0) AS first_quote, if(get_json_object(d4, '$.comment_level') IN ('1', '2'),op_cnt, 0) AS second_quote, op_cnt AS total_quote FROM hlw.t_dw_dc01160 WHERE tdbank_imp_date BETWEEN 2020063000 AND 2020063023 AND op_type='0X8009669' AND op_cnt<10 AND get_json_object(d4, '$.actionsheet_choose')='1' ) WHERE uin IS NOT NULL GROUP BY uin, op_type, nvl(source_type, '未知') DISTRIBUTE BY rand();
    # """

    sql = """
    INSERT  INTO  t_app_qb_weishi_play_user_d PARTITION (imp_date= 20200630) WITH guid_t AS (SELECT max(imei_idfa) imei, guid FROM omg_mobile_newsdev.t_imei_idfa_to_guid WHERE ds=20200630 GROUP BY guid), vid_t as (SELECT DISTINCT qq_browser_vid vid FROM pcg_weishi_application.ods_cp_push_video WHERE imp_date=20200630 ), play_t AS (SELECT guid, news_id, trim(regexp_extract(qua, 'PL=([^&]+)', 1)) platform, trim(regexp_extract(qua, 'MO=([^&]+)', 1)) dev_model, access_time event_time FROM pcg_txkd_qb_info_app.t_dwd_qb_video_play_flow_h WHERE p_datehour BETWEEN 2020063000 AND 2020063023 ) SELECT /*+mapjoin(vid_t)*/ 20200630 imp_date, 'QB' app, '0_19' app_channel_id_1, 'QB-feeds' app_channel_name_1, max(if(platform='IOS', 'ios', 'android')) os, '-' qimei, imei UID, min(event_time) event_time, 'video_play' event_id, max(dev_model) brand, vid_t.vid vid FROM vid_t JOIN play_t ON vid_t.vid = play_t.news_id LEFT JOIN guid_t ON guid_t.guid=play_t.guid GROUP BY imei, vid_t.vid;
"""

    print(sql)
    print("\n" + "-" * 160 + "\n")
    # sql = solve_less_alias_problem(sql)
    # sql = add_quote_on_date_for_DATE_ADD(sql)
    # sql = add_quote_on_date_for_DATE_SUB(sql)
    # sql = mysql2sql(sql)
    # sql = remove_overwrite_table(sql)
    sql = remove_partition_part(sql)
    print(sql)


if __name__ == '__main__':
    config_path = os.getcwd() + '/../james_config/james_config.conf'
    CO = configobj.ConfigObj(config_path)

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
