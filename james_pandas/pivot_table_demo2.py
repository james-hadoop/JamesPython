import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)

df = pd.read_csv('../_data/account_top200.csv')

df = df[df.puin.isin(['2713129639'])]

data = df[['s_input_date', 'week_of_year', 'input_week_day', 'cnt']]

table = data.pivot_table(index='week_of_year', columns='input_week_day')
# print(table)
print(table[0:])
print(table[:0])

# fig = plt.figure(figsize=(10, 6))
# colors = ['red', 'blue', 'green', 'orange', 'black', 'red', 'blue', 'green', 'orange', 'black']
#
# for i in range(10):
#     start_index = 33 + i
#     end_index = 33 + i
#     subset = table[start_index:end_index]
#     label = 'week-%s' % (i)
#     plt.plot(subset['week_of_year'], subset['cnt'], c=colors[i], label=label)
#
# plt.legend(loc='best')
# plt.show()
