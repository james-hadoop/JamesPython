import sys
import pandas as pd


def main():
    f1 = [1.560, 0.346, 1.380, 0.520, 0.795]
    f2 = [-0.605, 2.158, 0.231, 1.151, -0.226]

    arr = {"f1": f1,
           "f2": f2}

    df = pd.DataFrame(arr)
    print(df)
    # print('-'*160)
    # print(df.describe())


if __name__ == '__main__':
    pd.set_option('display.max_columns', 1000)

    pd.set_option('display.width', 1000)

    pd.set_option('display.max_colwidth', 1000)

    pd.set_option('display.max_rows', None)

    main()
    sys.exit(0)
