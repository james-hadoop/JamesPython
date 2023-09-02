"""
====================================================================
Author: James Jiang
====================================================================
"""

import sqlparse

SQL = """
INSERT INTO 

kandian_ods_video_core_d 
                    SELECT 20200608 AS ftime, rowkey, SUM(onetothree_expose) 
            AS onetothree_expose , SUM(onetothree_vv) AS onetothree_vv, SUM(tot_vv) AS tot_vv , SUM(tot_vv_incwesee) AS tot_vv_incwesee, AVG(mediaduration) AS mediaduration , SUM(sum_watchduration) / SUM(tot_vv) AS watchduration , AVG(watchduration) / AVG(mediaduration) AS watchratio , CASE  WHEN SUM(tot_vv) > 100 THEN SUM(valid_vv) / SUM(tot_vv) ELSE NULL END AS valid_ratio, SUM(valid_vv) AS valid_vv FROM kandian_ods_video_core_h WHERE fhour BETWEEN 2020060800 AND 2020060823 AND rowkey RLIKE '[0-9a-zA-Z]+' GROUP BY rowkey;

"""

SQL = """
INSERT INTO kandian_mid_video_cinfo_d  
    SELECT
        20200607 as ftime
        ,rowkey
        ,NVL(SUM(main_expose),0)
        ,NVL(SUM(tot_vv),0)
        ,NVL(SUM(tot_vv_incwesee),0)
        ,NVL(SUM(main_click),0)
        ,NVL(SUM(kddaily_expose),0)
        ,NVL(SUM(kddaily_click),0)
        ,NVL(SUM(tot_comment),0)
        ,NVL(SUM(dianzan),0)
        ,NVL(SUM(share),0)
        ,NVL(SUM(biu_bak),0)
        ,NVL(SUM(accuse),0)
        ,NVL(SUM(collect),0)
        ,NVL(SUM(comment_zan),0)
        ,NVL(SUM(main_ratio),0)
        ,NVL(SUM(kddaily_ratio),0)
        ,NVL(SUM(videochn_expose),0)
        ,NVL(SUM(videochn_click),0)
        ,NVL(SUM(videochn_ratio),0)
        ,NVL(SUM(otherchn_expose),0)
        ,NVL(SUM(otherchn_click),0)
        ,NVL(SUM(otherchn_ratio),0)
        ,NVL(SUM(main_comment),0)
        ,NVL(SUM(sub_comment),0)
        ,NVL(SUM(main_comment_zan),0)
        ,NVL(SUM(sub_comment_zan),0)
        ,NVL(SUM(cancel_dianzan),0)
        ,NVL(SUM(onetothree_expose),0)
        ,NVL(SUM(onetothree_vv),0)
        ,NVL(SUM(mediaduration),0)
        ,NVL(SUM(watchduration),0)
        ,NVL(SUM(watchratio),0)
        ,NVL(SUM(valid_ratio),0)
        ,NVL(SUM(all_neg_fback),0)
        ,NVL(SUM(onetothree_neg_fback),0)
        ,NVL(SUM(feeds_neg_fback),0)
        ,NVL(SUM(valid_vv),0) AS valid_vv
    FROM
        (
            SELECT a.* FROM
            (
                SELECT
                  rowkey
                  ,SUM(main_expose) AS main_expose
                  ,SUM(main_click) AS main_click
                  ,SUM(main_ratio) AS main_ratio
                  ,SUM(kddaily_expose) AS  kddaily_expose -- 20191022新口径
                  ,SUM(kddaily_click) AS kddaily_click -- 20191022新口径
                  ,SUM(kddaily_ratio) AS kddaily_ratio
                  ,SUM(videochn_expose) AS videochn_expose
                  ,SUM(videochn_click) AS videochn_click
                  ,SUM(videochn_ratio) AS videochn_ratio
                  ,SUM(otherchn_expose) AS otherchn_expose
                  ,SUM(otherchn_click) AS otherchn_click
                  ,SUM(otherchn_ratio) AS otherchn_ratio
                  ,SUM(comment_zan) AS comment_zan
                  ,SUM(main_comment) AS main_comment
                  ,SUM(sub_comment) AS sub_comment
                  ,SUM(tot_comment) AS tot_comment
                  ,SUM(main_comment_zan) AS main_comment_zan
                  ,SUM(sub_comment_zan) AS sub_comment_zan
                  ,NULL AS onetothree_expose
                  ,NULL AS onetothree_vv
                  ,NULL AS tot_vv
                  ,NULL AS tot_vv_incwesee
                  ,NULL AS mediaduration
                  ,NULL AS watchduration
                  ,NULL AS watchratio
                  ,NULL AS valid_ratio
                  ,NULL AS dianzan
                  ,NULL AS cancel_dianzan
                  ,SUM(biu_bak) AS biu_bak
                  ,NULL AS share
                  ,NULL AS collect
                  ,NULL AS accuse
                  ,NULL AS all_neg_fback
                  ,NULL AS onetothree_neg_fback
                  ,NULL AS feeds_neg_fback
                  ,NULL AS valid_vv
                FROM
                (
                   SELECT
                      rowkey
                      ,main_expose
                      ,main_click
                      ,main_ratio
                      ,kddaily_expose
                      ,kddaily_click
                      ,kddaily_ratio
                      ,videochn_expose
                      ,videochn_click
                      ,videochn_ratio
                      ,otherchn_expose
                      ,otherchn_click
                      ,otherchn_ratio
                      ,NULL AS comment_zan
                      ,NULL AS main_comment
                      ,NULL AS sub_comment
                      ,NULL AS tot_comment
                      ,NULL AS main_comment_zan
                      ,NULL AS sub_comment_zan
                      ,NULL AS biu_bak
                      ,NULL AS new_ribao_expose
                      ,NULL AS new_ribao_click
                   FROM kandian_ods_all_feeds_expclick_d
                   WHERE ftime = 20200607

                   UNION ALL

                   SELECT
                      rowkey
                      ,NULL AS  main_expose
                      ,NULL AS  main_click
                      ,NULL AS  main_ratio
                      ,NULL AS  kddaily_expose
                      ,NULL AS  kddaily_click
                      ,NULL AS  kddaily_ratio
                      ,NULL AS  videochn_expose
                      ,NULL AS  videochn_click
                      ,NULL AS  videochn_ratio
                      ,NULL AS  otherchn_expose
                      ,NULL AS  otherchn_click
                      ,NULL AS  otherchn_ratio
                      ,comment_zan
                      ,main_comment
                      ,sub_comment
                      ,tot_comment
                      ,main_comment_zan
                      ,sub_comment_zan
                      ,NULL AS biu_bak
                      ,NULL AS new_ribao_expose
                      ,NULL AS new_ribao_click
                    FROM kandian_ods_all_comment_comzan_d
                    where ftime = 20200607

                  UNION ALL

                  SELECT
                     rowkey
                     ,NULL AS main_expose
                     ,NULL AS main_click
                     ,NULL AS main_ratio
                     ,NULL AS kddaily_expose
                     ,NULL AS kddaily_click
                     ,NULL AS kddaily_ratio
                     ,NULL AS videochn_expose
                     ,NULL AS videochn_click
                     ,NULL AS videochn_ratio
                     ,NULL AS otherchn_expose
                     ,NULL AS otherchn_click
                     ,NULL AS otherchn_ratio
                     ,NULL AS comment_zan
                     ,NULL AS main_comment
                     ,NULL AS sub_comment
                     ,NULL AS tot_comment
                     ,NULL AS main_comment_zan
                     ,NULL AS sub_comment_zan
                     ,publish_biu AS biu_bak
                     ,NULL AS new_ribao_expose
                     ,NULL AS new_ribao_click
                  FROM kandian_ods_all_biu_d
                  where ftime = 20200607


                  UNION ALL

                  SELECT
                     rowkey
                     ,NULL AS main_expose
                     ,NULL AS main_click
                     ,NULL AS main_ratio
                     ,NULL AS kddaily_expose
                     ,NULL AS kddaily_click
                     ,NULL AS kddaily_ratio
                     ,NULL AS videochn_expose
                     ,NULL AS videochn_click
                     ,NULL AS videochn_ratio
                     ,NULL AS otherchn_expose
                     ,NULL AS otherchn_click
                     ,NULL AS otherchn_ratio
                     ,NULL AS comment_zan
                     ,NULL AS main_comment
                     ,NULL AS sub_comment
                     ,NULL AS tot_comment
                     ,NULL AS main_comment_zan
                     ,NULL AS sub_comment_zan
                     ,NULL AS biu_bak
                     ,new_ribao_expose
                     ,new_ribao_click
                  FROM kandian_ods_all_ribao_feeds_d
                  WHERE ftime = 20200607


                  )
                GROUP BY rowkey
            )a

          JOIN

          (
            SELECT
                rowkey
            FROM sng_mp_etldata.t_kd_video_info
            WHERE f_date = 20200607
          )b
          on a.rowkey = b.rowkey

          UNION ALL

          SELECT
             rowkey
             ,NULL AS main_expose
             ,NULL AS main_click
             ,NULL AS main_ratio
             ,NULL AS kddaily_expose
             ,NULL AS kddaily_click
             ,NULL AS kddaily_ratio
             ,NULL AS videochn_expose
             ,NULL AS videochn_click
             ,NULL AS videochn_ratio
             ,NULL AS otherchn_expose
             ,NULL AS otherchn_click
             ,NULL AS otherchn_ratio
             ,NULL AS comment_zan
             ,NULL AS main_comment
             ,NULL AS sub_comment
             ,NULL AS tot_comment
             ,NULL AS main_comment_zan
             ,NULL AS sub_comment_zan
             ,onetothree_expose
             ,onetothree_vv
             ,tot_vv
             ,tot_vv_incwesee
             ,mediaduration
             ,watchduration
             ,watchratio
             ,valid_ratio
             ,NULL AS dianzan
             ,NULL AS cancel_dianzan
             ,NULL AS biu_bak
             ,NULL AS share
             ,NULL AS collect
             ,NULL AS accuse
             ,NULL AS all_neg_fback
             ,NULL AS onetothree_neg_fback
             ,NULL AS feeds_neg_fback
             ,valid_vv
          from kandian_ods_video_core_d
          where ftime = 20200607

          UNION ALL

          SELECT
             rowkey
             ,NULL AS main_expose
             ,NULL AS main_click
             ,NULL AS main_ratio
             ,NULL AS kddaily_expose
             ,NULL AS kddaily_click
             ,NULL AS kddaily_ratio
             ,NULL AS videochn_expose
             ,NULL AS videochn_click
             ,NULL AS videochn_ratio
             ,NULL AS otherchn_expose
             ,NULL AS otherchn_click
             ,NULL AS otherchn_ratio
             ,NULL AS comment_zan
             ,NULL AS main_comment
             ,NULL AS sub_comment
             ,NULL AS tot_comment
             ,NULL AS main_comment_zan
             ,NULL AS sub_comment_zan
             ,NULL AS onetothree_expose
             ,NULL AS onetothree_vv
             ,NULL AS tot_vv
             ,NULL AS tot_vv_incwesee
             ,NULL AS mediaduration
             ,NULL AS watchduration
             ,NULL AS watchratio
             ,NULL AS valid_ratio
             ,dianzan
             ,cancel_dianzan
             ,biu_bak
             ,share
             ,collect
             ,accuse
             ,NULL AS all_neg_fback
             ,NULL AS onetothree_neg_fback
             ,NULL AS feeds_neg_fback
             ,NULL AS valid_vv
          from kandian_ods_video_interactive_d
          where ftime = 20200607

          UNION ALL

          SELECT
             rowkey
             ,NULL AS main_expose
             ,NULL AS main_click
             ,NULL AS main_ratio
             ,NULL AS kddaily_expose
             ,NULL AS kddaily_click
             ,NULL AS kddaily_ratio
             ,NULL AS videochn_expose
             ,NULL AS videochn_click
             ,NULL AS videochn_ratio
             ,NULL AS otherchn_expose
             ,NULL AS otherchn_click
             ,NULL AS otherchn_ratio
             ,NULL AS comment_zan
             ,NULL AS main_comment
             ,NULL AS sub_comment
             ,NULL AS tot_comment
             ,NULL AS main_comment_zan
             ,NULL AS sub_comment_zan
             ,NULL AS onetothree_expose
             ,NULL AS onetothree_vv
             ,NULL AS tot_vv
             ,NULL AS tot_vv_incwesee
             ,NULL AS mediaduration
             ,NULL AS watchduration
             ,NULL AS watchratio
             ,NULL AS valid_ratio
             ,NULL AS dianzan
             ,NULL AS cancel_dianzan
             ,NULL AS biu_bak
             ,NULL AS share
             ,NULL AS collect
             ,NULL AS accuse
             ,all_neg_fback
             ,onetothree_neg_fback
             ,feeds_neg_fback
             ,NULL AS valid_vv
          from kandian_ods_video_neg_feedback_d
          where ftime = 20200607
        )
        group by rowkey
        ;
"""

FORMATTED_SQL = sqlparse.format(SQL, reindent=False, keyword_case='upper')
print(FORMATTED_SQL)

COMPACTED_SQL = ''.join(FORMATTED_SQL.split())
print("-" * 100)
print(COMPACTED_SQL)
