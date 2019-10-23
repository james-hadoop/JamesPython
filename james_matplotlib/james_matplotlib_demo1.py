import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('../_data/account_top200.csv')
unrate = unrate[unrate.puin.isin(['2713129639'])]

fig = plt.figure(figsize=(10, 6))
colors = ['red', 'blue', 'green', 'orange', 'black']

for i in range(5):
    start_index = i * 12
    end_index = (i + 1) * 12
    subset = unrate[start_index:end_index]
    label = str(1948 + i)
    plt.plot(subset['input_date'], subset['cnt'], c=colors[i], label=label)

plt.legend(loc='best')
plt.show()
