import pandas as pd

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)

df = pd.read_csv('puin_top100_input.csv')

# df = df[df.puin.isin(['2713129639', '2269829235', '1685161793', '1685161748'])]

data = df[df.puin.isin(['2713129639']) & df.input_week_day.isin(['6'])]

data = data.sort_index(axis=0, by='input_date', ascending=True)

print(data)

data = data[data['input_date'] < 20191010]

# data = data[data['cnt'] > data.cnt.describe()['25%']]
# data = data[data['cnt'] < data.cnt.describe()['75%']]

data = data[['input_date', 'cnt']]

data.to_csv('2.csv')

# print(data.cnt.describe())
#
# print(data.cnt.describe()['25%'])
