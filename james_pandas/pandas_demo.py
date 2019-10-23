import pandas as pd

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)

df = pd.read_csv('../_data/account_top200.csv')

print(df.weekofyear.describe())

# df = df[df.puin.isin(['2713129639', '2269829235', '1685161793', '1685161748'])]

df = df[df.puin.isin(['1781806734'])]

# print(df.groupby(['puin', 'input_date']).cnt.describe()['max'])

# print(df.groupby(['puin', 'weekofyear', 'input_week_day']).cnt.agg('sum'))

# print(df.groupby(['puin', 'input_week_day']).cnt.describe())

print(df.groupby(['puin', 'input_date']).cnt.agg('sum'))
