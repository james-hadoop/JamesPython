# -*- coding: utf-8 -*-
import datetime
import inspect
import json
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)

df = pd.read_csv('../_data/20191027/content_20191027_top200.csv')

df = df[df.puin.isin(['2713129639'])]

data = df[['s_input_date', 'week_of_year', 'input_week_day', 'cnt']]
data = data[data['week_of_year'] > 36]
data = data[data['week_of_year'] < 43]

ret = data.groupby(['week_of_year']).cnt.mean()
ret.to_csv('../_data/20191027/week_of_year_mean.csv', header=False)
print(ret)

fig = plt.figure(figsize=(10, 6))
colors = ['red', 'blue', 'green', 'orange', 'black', 'cyan', 'darkgreen', 'darkred', 'gold']

df = pd.read_csv('_data/20191027/week_of_year_mean.csv', header=None)
print(df)
df.columns = ['week_of_year', 'cnt']
df.sort_values(axis=0, by=['week_of_year'], ascending=True)
print(df)

plt.plot(df['week_of_year'], df['cnt'])
plt.xticks(rotation=60)
plt.ylabel('content count')
plt.xlabel('week_of_year')
plt.title('week_of_year_sum')
plt.show()
