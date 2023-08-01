# -*- coding: utf-8 -*-
import pandas as pd

import sqlalchemy as sa
from matplotlib import pyplot as plt
from scipy.stats import zscore


# 将数据进行归一化，目的是让 dataframe 中的两列在同一量纲下比较
def minmax_norm(df, col):
    df[f"NORM_{col}"] = (df[col] - df[col].min()) / (
            df[col].max() - df[col].min())
    return df


def do_analysis(df, date_dim, metric_1, metric_2):
    # 删除 NaN 值
    df.dropna(inplace=True)

    minmax_norm(df, metric_1)
    minmax_norm(df, metric_2)
    print(df.head(5))

    df = df.sort_values(axis=0, by=[date_dim], ascending=True)
    # df_zscore = zscore(df[metric_1])

    # 将出租车订单数和新增确诊人数在同一量纲下绘图
    plt.figure(figsize=(10, 6))
    plt.plot(df[date_dim], df[f"NORM_{metric_1}"], c='deepskyblue', label=metric_1)
    plt.plot(df[date_dim], df[f"NORM_{metric_2}"], c='red', label=metric_2)

    plt.legend(loc='upper left')
    plt.title('data trend')
    plt.ylabel('')
    plt.xlabel('date')
    plt.xticks(rotation=60)

    plt.show()


def query_date_from_kylin(sql):
    kylin_engine = sa.create_engine(
        'kylin://ADMIN:KYLIN@123.57.213.244:7070/qimao_bigdata?pool_size=10&max_overflow=20&version=v4&prefix=/kylin/api')

    df = pd.read_sql(sql, kylin_engine)
    return df


def main():
    # 配置要查询的 SQL
    sql = '''
SELECT  DWT_MKT_QM_USER_CHANNEL_BAHAVIOR_INC_D.PROJECT
       ,SUM(DWT_MKT_QM_USER_CHANNEL_BAHAVIOR_INC_D.CURRENT_READ_DURATION) AS CURRENT_READ_DURATION
FROM DWT_MKT_QM_USER_CHANNEL_BAHAVIOR_INC_D
WHERE dt = '2022-12-01'
GROUP BY  DWT_MKT_QM_USER_CHANNEL_BAHAVIOR_INC_D.PROJECT;
        '''

    # 配置日期分区列
    date_dim = 'PICKUP_DATE'
    # 配置指标 1
    metric_1 = 'TAXI_ORDER_NUMBER'
    # 配置指标 2
    metric_2 = 'PEOPLE_POSITIVE_NEW_CASES_COUNT'

    # 通过 kylinpy，向 KE 查询数据
    df = query_date_from_kylin(sql)
    print(df)

    # 通过 KE 返回的数据，绘制数据趋势图
    # do_analysis(df, date_dim, metric_1, metric_2)


if __name__ == '__main__':
    # pandas 配置
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 10000)
    pd.set_option('display.max_colwidth', 1000)
    pd.set_option('display.max_rows', None)

    # 业务逻辑
    main()
