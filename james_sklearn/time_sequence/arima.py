import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.tsa.api as smt

import seaborn as sns

pd.set_option('display.float_format', lambda x: '%.5f' % x)
np.set_printoptions(precision=5, suppress=True)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

sns.set(style='ticks', context='poster')


def tsplot(y, lags=None, title='', figsize=(14, 8)):
    fig = plt.figure(figsize=figsize)
    layout = (2, 2)
    ts_ax = plt.subplot2grid(layout, (0, 0))
    hist_ax = plt.subplot2grid(layout, (0, 1))
    acf_ax = plt.subplot2grid(layout, (1, 0))
    pacf_ax = plt.subplot2grid(layout, (1, 1))

    y.plot(ax=ts_ax)
    ts_ax.set_title(title)
    y.plot(ax=hist_ax, kind='hist', bins=25)
    hist_ax.set_title('Histogram')
    smt.graphics.plot_acf(y, lags=lags, ax=acf_ax)
    smt.graphics.plot_pacf(y, lags=lags, ax=pacf_ax)
    [ax.set_xlim(0) for ax in [acf_ax, pacf_ax]]
    sns.despine()
    plt.tight_layout()
    return ts_ax, acf_ax, pacf_ax


df = pd.DataFrame(np.random.randn(600), index=pd.date_range('7/1/2016', periods=600, freq='D'), columns=['value'])

n_sample = df.shape[0]
print(n_sample)
print("-" * 120)

n_train = int(0.95 * n_sample) + 1
n_forecast = n_sample - n_train
ts_train = df.iloc[:n_train]['value']
ts_test = df.iloc[n_train:]['value']
print("Training Series:", "\n", ts_train.tail(), "\n")
print("Testing Series:", "\n", ts_test.head())
print("-" * 120)

tsplot(ts_train, title='A Given Training Series', lags=20)
plt.show()

arima200 = sm.tsa.SARIMAX(ts_train, order=(2, 0, 0))
model_results = arima200.fit()
