# -*- coding: utf-8 -*-
import os
import datetime
import logging as log
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from py_kd_data_common_proj.ds_utils.ds_common_util import (
    init_log_config,
    init_pandas_setting,
)

from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import layers


def str_to_datetime(s):
    split = s.split("-")
    year, month, day = int(split[0]), int(split[1]), int(split[2])

    return datetime.datetime(year=year, month=month, day=day)


def df_to_windowed_df(dataframe, first_date_str, last_date_str, n=3):
    first_date = str_to_datetime(first_date_str)
    last_date = str_to_datetime(last_date_str)

    target_date = first_date

    dates = []
    X, Y = [], []

    last_time = False
    while True:
        df_subset = dataframe.loc[:target_date].tail(n + 1)

        if len(df_subset) != n + 1:
            print(f"Error: Window of size {n} is too large for date {target_date}")
            return

        values = df_subset["Close"].to_numpy()
        x, y = values[:-1], values[-1]

        dates.append(target_date)
        X.append(x)
        Y.append(y)

        next_week = dataframe.loc[
                    target_date: target_date + datetime.timedelta(days=7)
                    ]
        next_datetime_str = str(next_week.head(2).tail(1).index.values[0])
        next_date_str = next_datetime_str.split("T")[0]
        year_month_day = next_date_str.split("-")
        year, month, day = year_month_day
        next_date = datetime.datetime(day=int(day), month=int(month), year=int(year))

        if last_time:
            break

        target_date = next_date
        if target_date == last_date:
            last_time = True

    ret_df = pd.DataFrame({})
    ret_df[("Target Date")] = dates

    X = np.array(X)
    for i in range(0, n):
        X[:, i]
        ret_df[f"Target-{n - i}"] = X[:, i]

    ret_df["Target"] = Y

    return ret_df


def windowed_df_to_date_X_y(windowed_dataframe):
    df_as_np = windowed_dataframe.to_numpy()
    dates = df_as_np[:, 0]
    middle_matrix = df_as_np[:, 1:-1]

    X = middle_matrix.reshape((len(dates), middle_matrix.shape[1], 1))
    Y = df_as_np[:, -1]

    return dates, X.astype(np.float32), Y.astype(np.float32)


def main():
    log.info("launch...")
    # df = pd.read_csv("D:/_AllDocMap/05_Dataset/MSFT_1y.csv")
    df = pd.read_csv("D:/_AllDocMap/05_Dataset/MSFT_max.csv")
    # print(df.head(5))

    df = df[["Date", "Close"]]
    print(df.head(5))

    datetime_object = str_to_datetime("2023-09-01")
    print(datetime_object)

    df["Date"] = df["Date"].apply(str_to_datetime)
    print(df["Date"])

    df.index = df.pop("Date")
    print(df)

    # plt.plot(df.index, df["Close"])
    # plt.show()

    windowed_df = df_to_windowed_df(df, "2021-09-28", "2023-09-28", n=3)
    print(windowed_df.head(5))

    dates, X, y = windowed_df_to_date_X_y(windowed_df)
    print(dates.shape, X.shape, y.shape)

    q_80 = int(len(dates) * 0.8)
    q_90 = int(len(dates) * 0.9)

    dates_train, X_train, y_train = dates[:q_80], X[:q_80], y[:q_80]
    dates_val, X_val, y_val = dates[q_80:q_90], X[q_80:q_90], y[q_80:q_90]
    dates_test, X_test, y_test = dates[q_90:], X[q_90:], y[q_90:]

    # plt.plot(dates_train, y_train)
    # plt.plot(dates_val, y_val)
    # plt.plot(dates_test, y_test)
    #
    # plt.legend(["Train", "Validation", "Test"])
    # plt.show()

    model = Sequential(
        [
            layers.Input((3, 1)),
            layers.LSTM(64),
            layers.Dense(32, activation="relu"),
            layers.Dense(32, activation="relu"),
            layers.Dense(1),
        ]
    )

    model.compile(
        loss="mse", optimizer=Adam(learning_rate=0.001), metrics=["mean_absolute_error"]
    )

    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=100)

    train_predictions = model.predict(X_train).flatten()
    plt.plot(dates_train, train_predictions)
    plt.plot(dates_train, y_train)
    # plt.legend(["Training Predictions", "Training Observations"])
    # plt.show()

    val_predictions = model.predict(X_val).flatten()
    plt.plot(dates_val, val_predictions)
    plt.plot(dates_val, y_val)
    # plt.legend(["Validation Predictions", "Validation Observations"])
    # plt.show()

    test_predictions = model.predict(X_test).flatten()
    plt.plot(dates_test, test_predictions)
    plt.plot(dates_test, y_test)
    # plt.legend(["Test Predictions", "Test Observations"])
    # plt.show()

    plt.legend(
        [
            "Training Predictions",
            "Training Observations",
            "Validation Predictions",
            "Validation Observations",
            "Test Predictions",
            "Test Observations",
        ]
    )
    plt.show()


if __name__ == "__main__":
    # 初始化pandas设置
    init_pandas_setting(pd)

    # 初始化日志打点设置
    LOG_FILE = os.path.basename(__file__).split(".")[0]
    LOG_TIME = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    FULL_LOG_PATH = (
            os.getcwd()
            + os.sep
            + ".."
            + os.sep
            + "logs"
            + os.sep
            + LOG_FILE
            + "_"
            + LOG_TIME
            + ".log"
    )
    init_log_config(log, FULL_LOG_PATH)

    # 业务逻辑
    main()

    # sys.exit(0)
