import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 1000)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', 1000)

pd.set_option('display.max_rows', None)

dims = ['11204', '11301', '11603', '11200', '12000', '11202'
        ]

# dims = [12701]

fig = plt.figure(figsize=(10, 6))
colors = ['red', 'darkorange', 'gold', 'green', 'cyan', 'deepskyblue', 'blueviolet', 'peru', 'brown', 'black']
i = 0

# df_kd = pd.read_csv('../_data/kd_video_lvyou_with_fans.csv')
# df_kb = pd.read_csv('../_data/kb_video_lvyou_with_fans.csv')
# df_qb = pd.read_csv('../_data/qb_video_lvyou_with_fans.csv')

# df_temp = df_kb.groupby('puin').size().to_frame().reset_index()
# df_temp.columns = ['puin', 'cnt']
# df_temp = df_temp.sort_values(by=['cnt'], ascending=False)
# df_temp = df_temp[df_temp['cnt'] > 1]
# print(df_temp)
# print("-" * 60)

# print("-" * 60)
# print(df_kd.columns)
# print(df_kb.columns
# print(df_qb.columns)
# print("-" * 60)

df_all = pd.read_csv('_data/sanduan_video_lvyou_with_fans.csv')
print(df_all.shape)
print("-" * 60)

# df_cnt = df_all.groupby('puin').size().to_frame().reset_index()
# df_cnt.columns = ['puin', 'cnt']
# df_cnt = df_cnt.sort_values(by=['cnt'], ascending=False)
# print(df_cnt.head(10))
# print("-" * 60)
#
# df_cnt = df_all.groupby('puin')['vv'].sum().to_frame().reset_index()
# df_cnt.columns = ['puin', 'vv']
# df_cnt = df_cnt.sort_values(by=['vv'], ascending=False)
# print(df_cnt.head(10))
# print("-" * 60)
#
# df_cnt = df_all.groupby('puin')['zan_cnt'].sum().to_frame().reset_index()
# df_cnt.columns = ['puin', 'zan_cnt']
# df_cnt = df_cnt.sort_values(by=['zan_cnt'], ascending=False)
# print(df_cnt.head(10))
# print("-" * 60)
#
# df_cnt = df_all.groupby('puin')['f_fans_cnt'].sum().to_frame().reset_index()
# df_cnt.columns = ['puin', 'f_fans_cnt']
# df_cnt = df_cnt.sort_values(by=['f_fans_cnt'], ascending=False)
# print(df_cnt.head(10))
# print("-" * 60)
#
# df_cnt = df_all.groupby('puin')['youzhi_cnt'].sum().to_frame().reset_index()
# df_cnt.columns = ['puin', 'youzhi_cnt']
# df_cnt = df_cnt.sort_values(by=['youzhi_cnt'], ascending=False)
# print(df_cnt.head(10))
# print("-" * 60)

df_all[df_all['zan_cnt']==0]=1
df_all[df_all['f_fans_cnt']==0]=1
df_all[df_all['youzhi_cnt']==0]=1

df_all['score'] = df_all['vv'] / 10000 * df_all['zan_cnt'] / 100 * df_all['f_fans_cnt'] / 50 * df_all['youzhi_cnt']


df_cnt = df_all.sort_values(by=['score'], ascending=False)
print(df_cnt.head(50))
print("-" * 120)
print(df_cnt[50:100])
# print("-" * 60)
# print(df_cnt[101:200])