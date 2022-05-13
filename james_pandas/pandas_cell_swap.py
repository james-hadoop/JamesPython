import pandas as pd
import numpy as np
import sys


def pandas_cell_func(x):
    if x == "nan, nan":
        return "_NULL"

    if not str(x).__contains__(","):
        return "_NULL"

    lat_lon = str(x).split(",")
    lat = lat_lon[0].strip()
    lon = lat_lon[1].strip()

    if float(lat) > 90.0:
        return f"{lon}, {lat}"
    else:
        return f"{lat}, {lon}"


def main():
    str0 = "nan, nan"
    str1 = "31.343, 123.3232"
    str2 = "123.3232, 31.343"
    str3 = "123.3232"

    print(pandas_cell_func(str0))
    print(pandas_cell_func(str1))
    print(pandas_cell_func(str2))


if __name__ == '__main__':
    pd.set_option('display.max_columns', 1000)

    pd.set_option('display.width', 1000)

    pd.set_option('display.max_colwidth', 1000)

    pd.set_option('display.max_rows', None)

    main()
    sys.exit(0)
