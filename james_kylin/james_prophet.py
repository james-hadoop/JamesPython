# -*- coding: utf-8 -*-
import datetime
import os

import numpy as np

from py_kd_data_common_proj.ds_utils import ds_date_util
from py_kd_data_common_proj.ds_utils.ds_common_util import init_log_config, init_pandas_setting, init_plot_setting

import pandas as pd
import matplotlib.pyplot as plt
import plotly
import logging as log

from py_kd_data_common_proj.ds_utils.ds_date_util import format_date

from fbprophet import Prophet
from fbprophet.plot import add_changepoints_to_plot


class suppress_stdout_stderr(object):
    '''
    A context manager for doing a "deep suppression" of stdout and stderr in
    Python, i.e. will suppress all print, even if the print originates in a
    compiled C/Fortran sub-function.
       This will not suppress raised exceptions, since exceptions are printed
    to stderr just before a script exits, and after the context manager has
    exited (at least, I think that is why it lets exceptions through).

    '''

    def __init__(self):
        # Open a pair of null files
        self.null_fds = [os.open(os.devnull, os.O_RDWR) for x in range(2)]
        # Save the actual stdout (1) and stderr (2) file descriptors.
        self.save_fds = (os.dup(1), os.dup(2))

    def __enter__(self):
        # Assign the null pointers to stdout and stderr.
        os.dup2(self.null_fds[0], 1)
        os.dup2(self.null_fds[1], 2)

    def __exit__(self, *_):
        # Re-assign the real stdout/stderr back to (1) and (2)
        os.dup2(self.save_fds[0], 1)
        os.dup2(self.save_fds[1], 2)
        # Close the null files
        os.close(self.null_fds[0])
        os.close(self.null_fds[1])


# 线上使用版本_二期 返回前端绘图数据
def formal_fbprophet_data(all_data, holidays, width=0.8):
    all_datas = all_data[['ftime', 'value']]
    all_datas.columns = ['ds', 'y']
    all_datas['ds'] = pd.to_datetime(all_datas['ds'], format='%Y%m%d')
    with suppress_stdout_stderr():
        fb_prophet = Prophet(changepoint_range=1 - round(7 / len(all_datas), 2),
                             changepoint_prior_scale=0.2, n_changepoints=round(len(all_datas) / 3),
                             interval_width=width, daily_seasonality=True, holidays_prior_scale=5)
        fb_prophet.fit(all_datas, iter=500)
        fb_forecast = fb_prophet.make_future_dataframe(periods=5, freq='D')
        fb_forecast = fb_prophet.predict(fb_forecast)

    # 输出预测图绘制相关数据
    f1 = fb_forecast[['ds', 'yhat', 'yhat_upper', 'yhat_lower']]
    h1 = fb_prophet.history[['ds', 'y']]
    axis_date = str(datetime.datetime.strftime(fb_prophet.history['ds'].max(), "%Y-%m-%d"))
    model_data = pd.merge(h1, f1, how='right', on='ds')

    # 判断异常点
    def if_anomaly(real, upper, lower):
        # if real > upper or real < lower:
        #     return 1
        # else:
        #     return -1
        return -1

    # 对于真实值输出数据的格式化
    def if_int(real):
        if real < 1:
            return round(real, 4)
        elif real > 100:
            return round(real)
        else:
            return round(real, 2)

    model_data['red_dot'] = model_data.apply(lambda x: if_anomaly(x.y, x.yhat_upper, x.yhat_lower), axis=1)
    model_data = model_data.fillna(-1)
    model_data = model_data[-80:]
    model_data['ds'] = model_data['ds'].astype(str)
    model_data['y'] = model_data['y'].apply(if_int)
    model_data = np.array(model_data).tolist()
    pic_data = str({"line_date": axis_date, 'model_Data': model_data}).replace("'", '"')
    return pic_data


def main():
    log.info("james_prophet")

    df = pd.read_csv(
        '/Users/qian.jiang/workspace4py/JamesPython/_data/kylin_demo/data/trip_data_2018-2021/2020/brief1-2020-12.csv', low_memory=False)
    log.info(df.head())

    stat_week_day_str_list = ds_date_util.make_stat_week_day_list('2020-01-01', -1, 7, 16, pattern='%Y-%m-%d')
    log.info(stat_week_day_str_list)

    df['pickup_date'] = df['tpep_pickup_datetime'].map(
        lambda x: str(format_date(x)))

    df['dropoff_date'] = df['tpep_dropoff_datetime'].map(
        lambda x: str(format_date(x)))

    df['ftime'] = df['tpep_pickup_datetime'].map(
        lambda x: str(format_date(x)))

    df['value'] = df['tolls_amount']

    all_datas = df
    log.info(all_datas.head())

    formal_fbprophet_data(all_datas, [])


if __name__ == '__main__':
    # 初始化 pandas 设置
    init_pandas_setting(pd)

    # 初始化 pyplot 设置
    init_plot_setting(plt)

    # print(os.getcwd())
    LOG_FILE = os.path.basename(__file__).split('.')[0]
    LOG_TIME = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    FULL_LOG_PATH = os.getcwd() + '/logs/' + LOG_FILE + '-' + LOG_TIME + '.log'
    print(f"FULL_LOG_PATH = {FULL_LOG_PATH}")

    # 初始化日志打点设置
    init_log_config(log, FULL_LOG_PATH, log_level=log.INFO)

    # 业务逻辑
    main()
