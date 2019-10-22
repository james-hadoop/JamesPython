# -*- encoding:utf-8 -*-
import sys

from sklearn import linear_model
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)

df = pd.read_csv('/Users/qjiang/workspace4python/JamesPython/james_pandas/2.csv')

X = np.array(df['input_date'])
X = X.tolist()

# 将点击量设为因变量Y
Y = np.array(df['cnt'])
Y = Y.tolist()

# ---------------------------------------------------------------
z1 = np.polyfit(X, Y, 2)  # 多项式拟合
p1 = np.poly1d(z1)
print("-" * 60)
print(z1)  # 多项式系数
print("-" * 60)
print(p1)
print("☆☆☆☆☆☆☆☆开始预测☆☆☆☆☆☆☆☆☆☆")
print(p1(20191012))
