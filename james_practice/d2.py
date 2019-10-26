import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 1000)
df = pd.DataFrame(data, columns=['x', 'y'])
print(df)

with sns.axes_style('white'):
    sns.jointplot(x='x', y='y', data=df, kind='hex', color='k')
    plt.show()
