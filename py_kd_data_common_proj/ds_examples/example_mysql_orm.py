# 1. 使用ds_assets/DDL_t_ds_demo.sql文件创建本地数据表
# 2. 获取配置参数文件ds_conf/config.conf中指定的库表信息
# 3. 使用sqlalchemy读取MySQL数据表t_ds_demo中的数据，并映射成对象TDsDemo
# 4. 操作TDsDemo对象，进行查询、聚合操作。
from datetime import datetime
import os

import configobj
from sqlalchemy import create_engine, Column, Integer, DateTime, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def main():
    config_path = os.getcwd() + '/../ds_conf/config.conf'
    CO = configobj.ConfigObj(config_path)

    LOCAL_DB = CO['LOCAL_DB']
    DB_HOST = CO['LOCAL_DB']['host']
    DB_USER = CO['LOCAL_DB']['user']
    DB_PASSWD = CO['LOCAL_DB']['passwd']
    DB_DB = CO['LOCAL_DB']['db']
    DB_PORT = CO['LOCAL_DB'].as_int('port')
    DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=UTF8MB4".format(username=DB_USER,
                                                                                               password=DB_PASSWD,
                                                                                               host=DB_HOST,
                                                                                               port=DB_PORT,
                                                                                               db=DB_DB)

    engine = create_engine(DB_URI)

    Base = declarative_base(engine)

    session = sessionmaker(engine)()

    # 定义对象TDsDemo与数据表t_ds_demo的映射关系
    class TDsDemo(Base):
        __tablename__ = 't_ds_demo'
        id = Column(Integer, primary_key=True, autoincrement=True)
        update_time = Column(DateTime, default=datetime.now())
        update_name = Column(String(20), nullable=False)
        value = Column(String(50), nullable=False)
        ext = Column(String(250), nullable=True)

        def __repr__(self):
            return "<TDsDemo(value:%s)>" % self.value

    # 获取指定全部数据
    results = session.query(TDsDemo).all()
    """
        <TDsDemo(value:i am a value@2020-04-04 12:06:41)>
        <TDsDemo(value:i am a value@2020-04-04 14:12:48)>
    """
    for ret in results:
        print(ret)

    print('-' * 80)
    # 获取部分字段
    results = session.query(TDsDemo.update_time, TDsDemo.update_name, TDsDemo.value).all()
    """
        (datetime.datetime(2020, 4, 1, 12, 6, 41), 'jamesqjiang', 'i am a value@2020-04-04 12:06:41')
        (datetime.datetime(2020, 4, 1, 14, 12, 48), 'jamesqjiang', 'i am a value@2020-04-04 14:12:48')
    """
    for ret in results:
        print(ret)

    print('-' * 80)
    # 获取记录条数
    cnt = session.query(func.count(TDsDemo.update_time)).first()
    """
        记录条数：2
    """
    print("记录条数：%s" % cnt)

    print('-' * 80)
    # 获取最新数据更新时间
    avg = session.query(func.max(TDsDemo.update_time)).first()
    """
        数据最新更新时间：2020-04-01 14:12:48
    """
    print("数据最新更新时间：%s" % avg)


if __name__ == '__main__':
    main()
