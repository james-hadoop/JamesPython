import base64
import re

# expression = 'J2tkJw=='
# clean_expression = re.sub('[\s+]', '', expression)
#
# bb = base64.decodebytes(clean_expression.encode())
# print(bb.decode("utf-8"))

# str = 'sng_mediaaccount_app.kandian_video_medium_full_info_d.kddaily_expose'
# src_table_name = str.rsplit('.', 1)[0]
# print(f"src_table_name={src_table_name}")

list_str=["0", "\tapplication_1589888927865_11666447:\nStage 0 succeeded:\n  Number of bytes read:          30026\n  Number of input records:       1318\n  Number of bytes written:       0\n  Number of output records:      0\n  Number of complete tasks:      1\n  Number of failed tasks:        0\n  Number of shuffle bytes read:  0\n  Number of shuffle record read: 0\n  Number of shuffle bytes write: 20\n  Number of shuffle record write:1\n  Total run time:                1798\n\tapplication_1589888927865_11666447:\nStage 1 succeeded:\n  Number of bytes read:          0\n  Number of input records:       0\n  Number of bytes written:       0\n  Number of output records:      1\n  Number of complete tasks:      1\n  Number of failed tasks:        0\n  Number of shuffle bytes read:  20\n  Number of shuffle record read: 1\n  Number of shuffle bytes write: 0\n  Number of shuffle record write:0\n  Total run time:                19809\n"]

print(list_str)
print(list_str[0])

sql_format="""
INSERT INTO t_dwt_consume_video_rowkeyperformance_normal_d
SELECT 20200607 AS ftime,
       'kd' AS sp_app_id,
       rowkey AS rowkey,
       NULL AS video_type,
       baoguang_cnt AS maintl_exp_cnt,
       main_click AS maintl_click_cnt,
       onetothree_expose AS floatlayer_exp_cnt,
       onetothree_vv AS floatlayer_vv,
       videochn_expose AS videochann_exp_cnt,
       videochn_click AS videochann_click_cnt,
       kddaily_expose AS infkddaily_exp_cnt,
       kddaily_click AS infkddaily_click_cnt,
       video_vv AS total_vv,
       valid_vv AS valid_vv,
       dianzan_cnt AS like_cnt,
       share_cnt AS share_cnt,
       biu_cnt AS biu_cnt,
       main_comment AS mainclass_cmt_cnt,
       main_comment_zan AS mainclass_cmtlike_cnt,
       sub_comment AS sub2class_cmt_cnt,
       sub_comment_zan AS sub2class_like_cnt,
       NULL AS collect_cnt,
       NULL AS accuse_cnt,
       NULL AS negfeeback_cnt,
       CAST(FLOOR(tot_watch_duration) AS BIGINT) AS duration_video
FROM sng_mediaaccount_app.kandian_video_medium_full_info_d
WHERE ftime = 20200607
"""

base64_encode = base64.encodebytes(sql_format.encode())
base64_decode = base64.decodebytes(base64_encode)
print(str(base64_decode))



