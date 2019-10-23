import pandas as pd

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)

df = pd.read_csv('../_data/account_top200.csv')

df = df[df.puin.isin(['2713129639'])]

table = df.pivot_table(index='week_of_year', columns='input_week_day')

print(table)
