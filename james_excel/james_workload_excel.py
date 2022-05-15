# coding:utf-8
import datetime
import sys
import openpyxl
import pandas as pd


def statistic_workload(excel_file_path):
    df = pd.read_excel(excel_file_path)

    columns = df.columns.values

    print("列名称")
    print(columns)
    print('-' * 16)

    # dataWeek = dataWeek.groupby(['union_chann_id', 's_cont_stat_date'])['today_ruku_cont_cnt'].sum()
    owner_df = df.groupby(['owner'])['工作摘要'].count()
    print("人-任务数")
    print(owner_df)
    print('-' * 64)

    owner_plan_df = df.groupby(['owner', '是否计划内'])['工作摘要'].count()
    print("人-是否计划内-任务数")
    print(owner_plan_df)
    print('-' * 64)

    print("任务记录日期")
    print(df['记录日期'])
    print('-' * 64)

    df['任务耗时'] = df['实际完成时间'] - df['记录日期']
    # df = df.eval('任务耗时=实际完成时间-记录日期', inplace=False)
    print("任务耗时")
    print(df)
    print('-' * 64)


def main():
    # print("Hello James!")

    excel_file_path = "/Users/qian.jiang/Downloads/KE PM工作 (1).xlsx"
    statistic_workload(excel_file_path)


if __name__ == '__main__':
    pd.set_option('display.max_columns', 1000)

    pd.set_option('display.width', 1000)

    pd.set_option('display.max_colwidth', 1000)

    pd.set_option('display.max_rows', None)

    main()
    sys.exit(0)
