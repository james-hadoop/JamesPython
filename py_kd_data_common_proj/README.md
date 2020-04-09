py_kd_data_common_proj
----------------------
py_kd_data_common_proj是一个python项目开发的脚手架，希望在ctrl_c和ctrl_v中开开心心学习数据科学项目开发。


py_kd_data_common_proj项目结构说明
--------------------------------
* ds_assets：存放公共资源文件，如SQL语句、图片文件。
* ds_conf：存放公共项目配置。
* ds_data：存放公共数据文件，如csv、excel文件。
* ds_examples：存放代码示例文件。
* ds_logs：存放公共日志文件。
* ds_utils：存放公共工具文件。
* jamesqjiang_app：存放个人应用代码。


ds_utils
--------
py_kd_data_common_proj项目中的ds_examples目录存放着公共工具文件。当前工具文件还比较少，希望在开发过程中，大家可以一起把各自经验、
心得添加到这个目录下，更加开心地在ctrl_c和ctrl_v中开发应用。

![ds_utils](ds_assets/pic/ds_utils.png)


ds_examples
-----------
py_kd_data_common_proj项目中的ds_examples目录提供了常用python应用相关示例，包含但不限于：
* 配置化参数：           ***example_get_config.py***
* 日志打点：             ***example_write_log.py***
* 数据库读写：           ***example_read_write_mysql_data.py***、***example_mysql_to_pandas.py***
* Mysql ORM：          ***example_mysql_orm.py***
* LZ任务执行情况查询：    ***example_get_lz_task_status.py***
* 企业微信告警：         ***example_send_wework_msg.py***
* 个人应用开发：         ***jamesqjiang_app***


个人应用开发
----------

![个人应用目录结构](ds_assets/pic/personal_app_structure.png)

在实际开发过程中，每个人的配置信息、数据文件、日志目录、代码逻辑可能是冲突的，因此可以新建一个以个人名义或者以
应用名称的子目录进行应用开发。
如上图，以jamesqjiang_app为例，来说明新建个人应用开发的子目录进行开发工作。
1. 新建应用子目录jamesqjiang_app，并且在该目录下创建conf（配置信息）、data（数据文件）、logs（日志目录）子目录。
2. 创建业务处理文件article_ruku_src_all_trend.py，该文件主要用来处理data/article_ruku_20200301.csv中的数据，画图。
3. article_ruku_src_all_trend.py用到了公共工具文件ds_utils目录下的ds_date_util.make_stat_week_day_list函数，
生成过去16周的周同比日期。
4.把数据集分成全量数据集和周同比数据集，并且根据维度进行聚合计算，最后生成如下走势图。

![来源内容量走势图](ds_assets/pic/src_cont_cnt_trend.png)
