import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

np.random.seed(sum(map(ord, 'regression')))

tips = sns.load_dataset('tips')
print(tips.head())

sns.regplot(x='total_bill', y='tip', data=tips)

sns.swarmplot(x='day', y='total_bill', hue='sex',
              data=tips)

sns.boxplot(x='day', y='total_bill', hue='time', data=tips)

plt.show()
