import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)

df = pd.read_csv('../_data/account_top200.csv')

df = df[df.puin.isin(['2713129639'])]

data = df[['s_input_date', 'week_of_year', 'input_week_day', 'cnt']]

ret = data.groupby(['week_of_year', 'input_week_day']).cnt.agg('sum')

ret = ret[3:]
ret = ret.rename(columns={'week_of_year', 'input_week_day', 'cnt'})
# ret.columns = ['week_of_year', 'input_week_day', 'cnt']
ret.to_csv('../_data/ret.csv')
# print(ret)

fig = plt.figure(figsize=(10, 6))
colors = ['red', 'blue', 'green', 'orange', 'black', 'red', 'blue', 'green', 'orange']

df = pd.read_csv('../_data/ret.csv')
# print(df)
df.columns = ['week_of_year', 'input_week_day', 'cnt']
# print(df)

for i in range(9):
    start_index = i * 7
    end_index = i * 7 + 7
    subset = df[start_index:end_index]
    print(subset)
    print('-' * 60)
    label = str(i)
    plt.plot(subset['input_week_day'], subset['cnt'], c=colors[i], label=label)

plt.legend(loc='best')
plt.show()