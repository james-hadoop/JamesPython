import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)

df = pd.read_csv('../_data/account_top200.csv')
# print(df)

df = df[df.puin.isin(['2713129639'])]
df = df[df['week_of_year'] > 33]
df = df[df['week_of_year'] < 43]
df = df.sort_values(axis=0, by=['week_of_year', 'input_week_day'], ascending=True)
# print(df)
df = df[['input_week_day', 'cnt']]
# print(data)

sns.boxplot(x='input_week_day', y='cnt', data=df)
