#! /bin/bash
############################################################
#AUTHOR         :jiangqian
#DESCRIBE       :dwt层每天用户 APP 活跃以及七猫 APP 阅读时长
#CREATE_DATE    :2022-11-22
############################################################
source /etc/profile

# 20221121
data_date=`date '+%Y%m%d' -d '-1 days'`
# 2022-11-21
input_date=`date '+%Y-%m-%d' -d '-1 days'`

#带参数时，以参数日期为准（手工修数）
if [ x$1 != x ]
then
    data_date=$1
    input_date=`date '+%Y-%m-%d' -d "${data_date}"`
fi

# 20221022
data_date_30=`date -d"30 day ago ${data_date}" +%Y%m%d`
# 2022-10-22
input_date_30=`date -d"30 day ago ${input_date}" +%Y-%m-%d`

# 20221115
data_date_7=`date -d"6 day ago ${data_date}" +%Y%m%d`
# 2022-11-15
input_date_7=`date -d"6 day ago ${input_date}" +%Y-%m-%d`

# 20221120
data_date_2=`date -d"1 day ago ${data_date}" +%Y%m%d`
# 2022-11-20
input_date_2=`date -d"1 day ago ${input_date}" +%Y-%m-%d`

# 20221122
current_date=`date '+%Y%m%d'`
base_work="/home/hadoop/bigdata"
sqoop_path="${base_work}/scripts/sqoop"
log_work="${base_work}/logs"
log_path="${log_work}/${current_date}"

#获取文件名剔除前后缀
script_name=${0##*/}
log_file="${log_path}/${script_name%.*}"`date +'%Y-%m-%d_%H:%M:%S'`".log"