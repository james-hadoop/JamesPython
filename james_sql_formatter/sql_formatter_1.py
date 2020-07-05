import re

import sqlparse

sql = """
INSERT INTO 

kandian_ods_video_core_d 
                    SELECT 20200608 AS ftime, rowkey, SUM(onetothree_expose) 
            AS onetothree_expose , SUM(onetothree_vv) AS onetothree_vv, SUM(tot_vv) AS tot_vv , SUM(tot_vv_incwesee) AS tot_vv_incwesee, AVG(mediaduration) AS mediaduration , SUM(sum_watchduration) / SUM(tot_vv) AS watchduration , AVG(watchduration) / AVG(mediaduration) AS watchratio , CASE  WHEN SUM(tot_vv) > 100 THEN SUM(valid_vv) / SUM(tot_vv) ELSE NULL END AS valid_ratio, SUM(valid_vv) AS valid_vv FROM kandian_ods_video_core_h WHERE fhour BETWEEN 2020060800 AND 2020060823 AND rowkey RLIKE '[0-9a-zA-Z]+' GROUP BY rowkey;

"""

sql_format = sqlparse.format(sql, reindent=True, keyword_case='upper')

print(sql_format)
sql_compact = ' '.join(sql_format.split())
print("-" * 160)
print(sql_compact)

sqlparse.v
