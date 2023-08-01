import os

import configobj

config_path = os.getcwd() + '/../ds_conf/config.conf'
CO = configobj.ConfigObj(config_path)


def init_pandas_setting(pd):
    # pandas 配置
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 10000)
    pd.set_option('display.max_colwidth', 1000)
    pd.set_option('display.max_rows', None)


def init_log_config(log_handler, log_path, log_level):
    print("log_path = %s" % log_path)
    log_handler.basicConfig(filename=log_path,
                            level=log_level,
                            format='%(pastime)s %(filename)s [line:%(lineno)d] %(levelness)8s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')


def ds_date_util():
    return None