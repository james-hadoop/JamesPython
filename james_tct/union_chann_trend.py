import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore

## pandas显示设置
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.max_rows', None)

## pyplot画布设置
TITLE = 'dim of chann'
Y_LABEL = 'qiyong content count'
fig = plt.figure(figsize=(10, 6))
colors = ['deepskyblue', 'blueviolet', 'peru', 'brown', 'black', 'red', 'gold', 'darkorange']
i = 0

## 过滤来源id
dims_src = []

## 指定分类id
dim = '118'

## 读取csv文件，生成dataframe
df = pd.read_csv('../_data/tct/article_qiyong_20200301.csv')

## 根据s_cont_stat_date过滤数据
data = df[df['s_cont_stat_date'] > '2019-01-23']

## 根据src过滤数据
if len(dims_src) != 0:
    data = data[data.src.isin(dims_src)]

## dataframe根据union_chann_id和s_cont_stat_date进行groupby，对today_ruku_cont_cnt求和，生成新的dataframe
data = data.groupby(['union_chann_id', 's_cont_stat_date'])['today_ruku_cont_cnt'].sum()
## 求和之后的列重命名
data = data.reset_index(name='today_ruku_cont_cnt')

## dataframe根据union_chann_id过滤数据
subset = data[data.union_chann_id.isin([dim])]

## dataframe根据's_cont_stat_date', 'union_chann_id'升序排序
subset = subset.sort_values(axis=0, by=['s_cont_stat_date', 'union_chann_id'], ascending=True)

## 计算today_ruku_cont_cnt的z_score
cnt_zscore = zscore(subset['today_ruku_cont_cnt'])
subset['cnt_zscore'] = cnt_zscore
print(subset)
print('-' * 120)

## 使用pyplot绘图
plt.plot(subset['s_cont_stat_date'], subset['today_ruku_cont_cnt'], c=colors[i], label=dim)

plt.legend(loc='upper left')
plt.title(TITLE)
plt.ylabel(Y_LABEL)
plt.xlabel('date')
plt.xticks(rotation=60)

plt.show()
