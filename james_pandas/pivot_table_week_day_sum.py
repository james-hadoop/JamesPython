import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)

df = pd.read_csv('../_data/20191027/content_20191027_top200.csv')
print(df.head(10))

df = df[df.puin.isin(['2713129639'])]

data = df[['s_input_date', 'week_of_year', 'input_week_day', 'cnt']]
data = data[data['week_of_year'] > 36]
data = data[data['week_of_year'] < 43]
print(data.head())

ret = data.groupby(['input_week_day']).cnt.mean()
ret.columns = ['input_week_day', 'cnt']
ret.to_csv('../_data/20191027/input_week_day_mean.csv', header=True)
print(ret)

fig = plt.figure(figsize=(10, 6))
colors = ['red', 'blue', 'green', 'orange', 'black', 'cyan', 'darkgreen', 'darkred', 'gold']

df = pd.read_csv('../_data/20191027/input_week_day_mean.csv')
print(df)
df.columns = ['input_week_day', 'cnt']
df.sort_values(axis=0, by=['input_week_day'], ascending=True)
print(df)

plt.plot(df['input_week_day'], df['cnt'])
plt.xticks(rotation=60)
plt.ylabel('content count')
plt.xlabel('input_week_day')
plt.title('input_week_day_sum')
plt.show()
