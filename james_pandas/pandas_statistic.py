import pandas as pd

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.max_rows', None)

df = pd.read_csv('puin_top100_input.csv')
# df = df[df.puin.isin(['2713129639', '2269829235', '1685161793', '1685161748'])]
data = df[df.puin.isin(['2713129639'])]
data = data.sort_values(axis=0, by='input_date', ascending=True)
data.to_csv('3.csv')

data = data.sort_values(axis=0, by='cnt', ascending=True)
data = data['cnt']
print(data)
print(data.median())
