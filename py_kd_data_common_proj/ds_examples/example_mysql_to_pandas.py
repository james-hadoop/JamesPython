# 1. 使用ds_assets/DDL_t_ds_demo.sql文件创建本地数据表
# 2. 获取配置参数文件ds_conf/config.conf中指定的库表信息
# 3. 使用sqlalchemy读取MySQL数据库中的数据，并且生成pandas data frame
# 4. 将pandas data frame中的数据存成csv文件ds_data/example_mysql_to_pandas.csv
# csv文件如下：
#
# ,id,update_time,update_name,value,ext
# 0,1,2020-04-01 12:06:41,jamesqjiang,i am a value@2020-04-01 12:06:41,{}
# 1,2,2020-04-01 14:12:48,jamesqjiang,i am a value@2020-04-01 14:12:48,{}
import os

import configobj
import pandas as pd
from sqlalchemy import create_engine

config_path = os.getcwd() + '/../ds_conf/config.conf'
CO = configobj.ConfigObj(config_path)


def main():
    LOCAL_DB = CO['LOCAL_DB']
    DB_HOST = CO['LOCAL_DB']['host']
    DB_USER = CO['LOCAL_DB']['user']
    DB_PASSWD = CO['LOCAL_DB']['passwd']
    DB_DB = CO['LOCAL_DB']['db']
    DB_PORT = CO['LOCAL_DB'].as_int('port')

    engine = create_engine("mysql+pymysql://%s:%s@%s:%s/%s" % (DB_USER, DB_PASSWD, DB_HOST, DB_PORT, DB_DB))

    sql_select = "select * from t_ds_demo where update_time;"
    df = pd.read_sql_query(sql_select, engine)
    print(df)
    df.to_csv('/home/james/workspace4py/JamesPython/py_kd_data_common_proj/ds_data/example_mysql_to_pandas.csv')


if __name__ == '__main__':
    main()
