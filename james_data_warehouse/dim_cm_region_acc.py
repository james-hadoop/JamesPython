import sys
import datetime
import calendar
import pandas as pd
import csv


def parse_dim_cc_info():
    path_dir = '/Users/jiangqian/Documents/_AllDocMap/02_Project/ws4python/JamesPython/_data'
    path_src = f"{path_dir}/dim_cm_region_acc_origin.csv"
    path_dst = f"{path_dir}/dim_cm_region_acc.csv"
    print(f"\npath_src={path_src}\npath_dst={path_dst}")

    df = pd.read_csv(path_src)
    print(df)

    # 取出需要调整顺序的列数据'D'
    df.pop('id')
    df.pop('region_id')
    df.pop('area_code')

    df['city'] = df['province'].map(
        lambda x: "")
    df['country'] = df['province'].map(
        lambda x: "中国")
    # df['region_str'] = df['province'].map(
    #     lambda x: f"_{x}_中国")

    df['region_str'] = df.apply(lambda x: str(x['city']) + "_" + str(x['province'] + "_中国"), axis=1)

    d = df.pop('region_str')
    df.insert(0, 'region_str', d)

    d = df.pop('iso_3166_1')
    df.insert(1, 'iso_3166_1', d)

    d = df.pop('iso_3166_2')
    df.insert(2, 'iso_3166_2', d)

    d = df.pop('city')
    df.insert(3, 'city', d)

    d = df.pop('province')
    df.insert(4, 'province', d)

    d = df.pop('country')
    df.insert(5, 'country', d)

    print(df)
    df.to_csv(path_dst, header=True, index=False)


def main():
    parse_dim_cc_info()


if __name__ == '__main__':
    # setting of padas
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 1000)
    pd.set_option('display.max_rows', None)

    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_colwidth', 1000)
    pd.set_option('display.max_rows', None)

    main()

    sys.exit(0)
