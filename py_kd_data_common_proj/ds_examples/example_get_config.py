# 根据指定配置参数文件的路径，通过configobj模块，自动将配置参数解析成参数字典。
# 配置参数的文件如下：
#
# [LOG]
# log_dir = /Users/qjiang/workspace4python/py_kd_data_common_proj/ds_logs/
#
# [LOCAL_DB]
# host	  = localhost
# user	  = developer
# passwd  = developer
# db      = cp_lz_output
# port	  = 3306
import os

import configobj

config_path = os.getcwd() + '/../ds_conf/config.conf'
CO = configobj.ConfigObj(config_path)


def main():
    LOCAL_DB = CO['LOCAL_DB']
    DB_HOST = CO['LOCAL_DB']['host']
    DB_USER = CO['LOCAL_DB']['user']
    DB_PASSWD = CO['LOCAL_DB']['passwd']
    DB_DB = CO['LOCAL_DB']['db']
    DB_PORT = CO['LOCAL_DB'].as_int('port')

    """
        LOCAL_DB={'host': 'localhost', 'user': 'developer', 'passwd': 'developer', 'db': 'cp_lz_output', 'port': '3306'}
        DB_HOST=localhost
        DB_USER=developer
        DB_PASSWD=developer
        DB_DB=cp_lz_output
        DB_PORT=3306
    """
    print("LOCAL_DB=%s" % LOCAL_DB)
    print("DB_HOST=%s" % DB_HOST)
    print("DB_USER=%s" % DB_USER)
    print("DB_PASSWD=%s" % DB_PASSWD)
    print("DB_DB=%s" % DB_DB)
    print("DB_PORT=%s" % DB_PORT)


if __name__ == '__main__':
    main()
