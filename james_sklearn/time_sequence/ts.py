import pandas as pd
import numpy as np
import datetime as dt

rng = pd.date_range('2019/07/01', periods=10, freq='D')
print(rng)
print("-" * 120)

time = pd.Series(np.random.randn(20), index=pd.date_range(dt.datetime(2016, 1, 1), periods=20))
print(time)
print(time['2016-01-10'])

time.truncate(before='2016-01-10' )
