import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)

# 样本数据集
# df = pd.Series([15.6, 16.2, 22.5, 20.5, 16.4, 19.4, 16.6, 17.9, 12.7, 13.9])
df = pd.Series([196974, 194575, 198208, 187449, 196998, 181180, 161038, 121300, 187112])
# df = df.reset_index(name='cnt')
# df = df.sort_values(axis=0, by=['cnt'], ascending=True)


# 样本平均值
sample_mean = df.mean()
# 样本标准差
sample_std = df.std()
print('样本平均值=', sample_mean, '单位：ppm')
print('样本标准差=', sample_std, '单位：ppm')

sns.distplot(df)
plt.title('Data Distribute')
plt.show()
