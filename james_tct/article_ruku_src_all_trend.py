# -*- coding: utf-8 -*-
import datetime
import inspect
import json
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import james_util.date_util as date_util
from scipy.stats import zscore

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)

TITLE = 'dim of chann'
Y_LABEL = 'jishen content count'

# union_chann_id=140 -> '壁纸头像'
# union_chann_id=134  -> '星座命理'
dims_src = []
dims_union_chann_id = ['118']

statWeekDayStrList = []
statWeekDayStrList = date_util.make_stat_week_day_str_list('2020-03-01', -1, 7, 16)

fig = plt.figure(figsize=(10, 6))
colors = ['deepskyblue', 'blueviolet', 'peru', 'brown', 'black', 'red', 'gold', 'darkorange']
i = 0

df = pd.read_csv('/Users/qian.jiang/workspace4py/JamesPython/_data/article_ruku_20200301.csv')
data = df[df['s_cont_stat_date'] > '2019-01-23']
dataWeek = data.copy()

if len(statWeekDayStrList) != 0:
    dataWeek = data[data.s_cont_stat_date.isin(statWeekDayStrList)]

if len(dims_src) != 0:
    data = data[data.src.isin(dims_src)]
    dataWeek = dataWeek[dataWeek.src.isin(dims_src)]

if len(dims_union_chann_id) == 0:
    dims_union_chann_id = ['102', '103', '104', '108', '110', '120']

data = data.groupby(['union_chann_id', 's_cont_stat_date'])['today_ruku_cont_cnt'].sum()
data = data.reset_index(name='today_ruku_cont_cnt')

dataWeek = dataWeek.groupby(['union_chann_id', 's_cont_stat_date'])['today_ruku_cont_cnt'].sum()
dataWeek = dataWeek.reset_index(name='today_ruku_cont_cnt')

# print('*' * 120)
# print(data)
# print('*' * 120)

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

    # subsetWeek = dataWeek[dataWeek.union_chann_id.isin([dim])]
    # subsetWeek = subsetWeek.sort_values(axis=0, by=['s_cont_stat_date', 'union_chann_id'], ascending=True)
    # print('-' * 60)
    # cnt_zscore_week = zscore(subsetWeek['today_ruku_cont_cnt'])
    # subsetWeek['cnt_zscore'] = cnt_zscore_week
    # print(subsetWeek)
    # print('')
    # plt.plot(subsetWeek['s_cont_stat_date'], subsetWeek['today_ruku_cont_cnt'], c=colors[i], label=dim)
    # i += 1

plt.legend(loc='upper left')
plt.title(TITLE)
plt.ylabel(Y_LABEL)
plt.xlabel('date')
plt.xticks(rotation=60)

plt.show()