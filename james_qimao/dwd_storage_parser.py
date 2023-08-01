# -*- coding: utf-8 -*-
import datetime
import os
import sys

import pandas as pd
import logging as log


def main():
    pass


if __name__ == '__main__':
    # pandas 配置
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 10000)
    pd.set_option('display.max_colwidth', 1000)
    pd.set_option('display.max_rows', None)

    # 业务逻辑
    main()

    sys.exit(0)
