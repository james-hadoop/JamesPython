import pandas as pd
import numpy as np
import datetime as dt

rng = pd.date_range('1/1/2011', periods=90, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts.head())
print("-" * 120)

print(ts.resample('M').sum())
print("-" * 120)

day3ts = ts.resample('3D').mean()
print(day3ts.resample('D').asfreq())
print("-" * 120)

print(day3ts.resample('D').interpolate('linear'))
print("-" * 120)
