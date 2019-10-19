import pandas as pd

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)

df = pd.read_csv('puin_top100_input.csv')

print(df.weekofyear.describe())

df = df[df.puin.isin(['2713129639', '2269829235', '1685161793', '1685161748'])]

# print(df.groupby(['puin', 'input_week_day']).cnt.describe())

print(df.groupby(['puin', 'weekofyear']).cnt.agg('sum'))


