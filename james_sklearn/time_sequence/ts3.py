import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.Series(np.random.randn(600), index=pd.date_range('7/1/2016', periods=600, freq='D'))
print(df.head())
print("-" * 120)

r = df.rolling(window=10)
print(r)
print(r.mean())
print("-" * 120)

plt.figure(figsize=(15, 5))
df.plot(style='r--')
df.rolling(window=10).mean().plot(style='b')
plt.show()
