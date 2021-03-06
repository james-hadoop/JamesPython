import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)

df = pd.read_csv('../_data/20191027/content_20191027_top200.csv')

df = df[df.puin.isin(['2713129639'])]

data = df[['s_input_date', 'week_of_year', 'input_week_day', 'cnt']]
data = data[data['week_of_year'] > 35]
data = data[data['week_of_year'] < 44]

ret = data.groupby(['week_of_year', 'input_week_day']).cnt.mean()
ret.columns = ['week_of_year', 'input_week_day', 'cnt']
ret.to_csv('../_data/20191027/ret_20191027.csv', header=False)
print(ret)

fig = plt.figure(figsize=(10, 6))
colors = ['red', 'blue', 'green', 'orange', 'black', 'cyan', 'darkgreen', 'darkred', 'gold']

df = pd.read_csv('../_data/20191027/ret_20191027.csv', header=None)
df.columns = ['week_of_year', 'input_week_day', 'cnt']
df.sort_values(axis=0, by=['week_of_year', 'input_week_day'], ascending=True)
print(df)

for i in range(8):
    print(i)
    print(colors[i])
    start_index = i * 7
    end_index = i * 7 + 7
    subset = df[start_index:end_index]
    print('-' * 60)
    print(subset)
    print('-' * 60)
    print('')
    label = 'week ' + str(35 + i + 1)
    plt.plot(subset['input_week_day'], subset['cnt'], c=colors[i], label=label)

plt.legend(loc='upper right')
plt.show()