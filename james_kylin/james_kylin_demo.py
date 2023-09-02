# -*- coding: utf-8 -*-
import datetime
import os
import sys

import pandas as pd
import logging as log

#from py_kd_data_common_proj.ds_utils.ds_common_util import init_log_config, init_pandas_setting


def main():
    covid_19_activity_file = "/home/james/_AllDocMap/05_Dateset/kylin_demo/data/covid19_data/t_covid_19_activity_202012.csv"
    taxi_activity_file = "/home/james/_AllDocMap/05_Dateset/kylin_demo/data/trip_data_2018-2021/2020/brief1-2020-12.csv"
    taxi_zone_file = "/home/james/_AllDocMap/05_Dateset/kylin_demo/data/taxi_zone/taxi_zone_lookup.csv"
    calendar_file = "/home/james/_AllDocMap/05_Dateset/kylin_demo/data/lookup_calendar/kylin_cal.csv"

    calendar_df = pd.read_csv(calendar_file)
    log.info(calendar_df.head(5))

    taxi_zone_df = pd.read_csv(taxi_zone_file)
    log.info(taxi_zone_df.head(5))

    # measure: total_amount
    # dim: PULocationID
    taxi_df = pd.read_csv(taxi_activity_file)
    log.info(taxi_df.head(5))

    # measure: PEOPLE_POSITIVE_NEW_CASES_COUNT, PEOPLE_DEATH_COUNT
    covid_df = pd.read_csv(covid_19_activity_file)
    log.info(covid_df.head(5))


if __name__ == '__main__':
    # 初始化pandas设置
    init_pandas_setting(pd)

    print(os.getcwd())
    LOG_FILE = os.path.basename(__file__).split('.')[0]
    LOG_TIME = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    FULL_LOG_PATH = os.getcwd() + '/logs/' + LOG_FILE + LOG_TIME + '.log'

    # 初始化日志打点设置
    init_log_config(log, FULL_LOG_PATH, log_level=log.INFO)

    # 业务逻辑
    main()

    sys.exit(0)
