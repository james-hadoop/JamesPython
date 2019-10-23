# -*- encoding:utf-8 -*-
import sys

from sklearn import linear_model
import numpy as np
import pandas as pd

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)

df = pd.read_csv('../_data/account_top200.csv')

# df = df[df.puin.isin(['2713129639', '2269829235', '1685161793', '1685161748', '1781806909'])]

data = df[df.puin.isin(['1781806909']) & df.input_week_day.isin(['5'])]

data_sample = data.sort_values(axis=0, by='input_date', ascending=True)

print(data_sample)

data = data[data['input_date'] < 20191010]

# data = data[data['cnt'] > data.cnt.describe()['25%']]
# data = data[data['cnt'] < data.cnt.describe()['75%']]

data = data[['input_date', 'cnt']]

data.to_csv('../_data/2.csv')

df = pd.read_csv('../_data/2.csv')

X = np.array(df['input_date'])
X = X.tolist()

# 将点击量设为因变量Y
Y = np.array(df['cnt'])
Y = Y.tolist()

# ---------------------------------------------------------------
z1 = np.polyfit(X, Y, 30)  # 多项式拟合
p1 = np.poly1d(z1)
print("-" * 60)
print(z1)  # 多项式系数
print("-" * 60)
print(p1)
print("☆☆☆☆☆☆☆☆开始预测☆☆☆☆☆☆☆☆☆☆")
print(data_sample[data_sample.input_date.isin(['20191011'])]['cnt'])
print(p1(20191011))
