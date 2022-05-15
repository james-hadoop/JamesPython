# -*- coding: utf-8 -*-
import datetime
import os

from py_kd_data_common_proj.ds_utils import ds_date_util

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore
import logging as log

from py_kd_data_common_proj.ds_utils.ds_common_util import init_log_config, init_pandas_setting


def main():
    TITLE = 'dim of chann'
    Y_LABEL = 'article ruku content count'

    # union_chann_id=118 -> '美食'
    dims_src = []
    dims_union_chann_id = ['118']

    statWeekDayStrList = []
    """
        生成一个日期列表。
        该日期列表是包含'2020-03-01'在内，'2020-03-01'的周同比日期（'2020-03-01'是周日）日期列表
        该日期列表生成16个元素
    """
    statWeekDayStrList = ds_date_util.make_stat_week_day_list('2020-03-01', -1, 7, 16, pattern='%Y-%m-%d')
    """
        [
            '2020-03-01', '2020-02-23', '2020-02-16', '2020-02-09', '2020-02-02', '2020-01-26', '2020-01-19',
            '2020-01-12', '2020-01-05', '2019-12-29', '2019-12-22', '2019-12-15', '2019-12-08', '2019-12-01', 
            '2019-11-24', '2019-11-17'
        ]
    """
    log.info(statWeekDayStrList)

    fig = plt.figure(figsize=(10, 6))
    colors = ['deepskyblue', 'blueviolet', 'peru', 'brown', 'black', 'red', 'gold', 'darkorange']
    i = 0

    df = pd.read_csv(
        '/Users/qian.jiang/workspace4py/JamesPython/_data/article_ruku_20200301.csv')
    data = df[df['s_cont_stat_date'] > '2019-01-23']
    # 深copy
    dataWeek = data.copy()

    if len(statWeekDayStrList) != 0:
        dataWeek = data[data.s_cont_stat_date.isin(statWeekDayStrList)]

    if len(dims_src) != 0:
        data = data[data.src.isin(dims_src)]
        dataWeek = dataWeek[dataWeek.src.isin(dims_src)]

    if len(dims_union_chann_id) == 0:
        dims_union_chann_id = ['102', '103', '104', '108', '110', '120']

    # 原始日期列表的聚合函数
    data = data.groupby(['union_chann_id', 's_cont_stat_date'])['today_ruku_cont_cnt'].sum()
    data = data.reset_index(name='today_ruku_cont_cnt')
    # log.info(data)

    # 生成日期列表的聚合函数
    dataWeek = dataWeek.groupby(['union_chann_id', 's_cont_stat_date'])['today_ruku_cont_cnt'].sum()
    dataWeek = dataWeek.reset_index(name='today_ruku_cont_cnt')
    # log.info(dataWeek)

    # 原始日期列表的数据和生成日期列表的数据画在同一张图中
    for dim in dims_union_chann_id:
        subset = data[data.union_chann_id.isin([dim])]
        subset = subset.sort_values(axis=0, by=['s_cont_stat_date', 'union_chann_id'], ascending=True)
        print('-' * 60)
        cnt_zscore = zscore(subset['today_ruku_cont_cnt'])
        subset['cnt_zscore'] = cnt_zscore
        print(subset)
        print('')
        plt.plot(subset['s_cont_stat_date'], subset['today_ruku_cont_cnt'], c=colors[i], label=dim)
        i += 1

        subsetWeek = dataWeek[dataWeek.union_chann_id.isin([dim])]
        subsetWeek = subsetWeek.sort_values(axis=0, by=['s_cont_stat_date', 'union_chann_id'], ascending=True)
        print('-' * 60)
        cnt_zscore_week = zscore(subsetWeek['today_ruku_cont_cnt'])
        subsetWeek['cnt_zscore'] = cnt_zscore_week
        print(subsetWeek)
        print('')
        plt.plot(subsetWeek['s_cont_stat_date'], subsetWeek['today_ruku_cont_cnt'], c=colors[i], label=dim)
        i += 1

    plt.legend(loc='upper left')
    plt.title(TITLE)
    plt.ylabel(Y_LABEL)
    plt.xlabel('date')
    plt.xticks(rotation=60)

    plt.show()


if __name__ == '__main__':
    # 初始化pandas设置
    init_pandas_setting(pd)

    print(os.getcwd())
    LOG_FILE = os.path.basename(__file__).split('.')[0]
    LOG_TIME = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    FULL_LOG_PATH = os.getcwd() + '/logs/' + LOG_FILE + LOG_TIME + '.log'
    print(f"FULL_LOG_PATH={FULL_LOG_PATH}")

    # 初始化日志打点设置
    init_log_config(log, FULL_LOG_PATH, log_level=log.INFO)

    # 业务逻辑
    main()
