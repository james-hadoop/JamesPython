import pandas as pd
import math
import matplotlib.pyplot as plt
from scipy.stats import zscore
import seaborn as sns

# df = pd.DataFrame({'cnt': [
#     197239,
#     204824,
#     204485,
#     203704,
#     202275,
#     145786,
#     126233,
#     196974,
#     200777,
#     201422,
#     200503,
#     195949,
#     141781,
#     119897,
#     194544,
#     213612,
#     202227,
#     211264,
#     200747,
#     139067,
#     126925,
#     198208,
#     198020,
#     197613,
#     199822,
#     199037,
#     139900,
#     123647,
#     187428,
#     193489,
#     130294,
#     190892,
#     193752,
#     135798,
#     117504,
#     196934,
#     207563,
#     207892,
#     204828,
#     200244,
#     134875,
#     120463,
#     181150,
#     186692,
#     184819,
#     181118,
#     174550,
#     123320,
#     145518,
#     160964,
#     153589,
#     143719,
#     126736,
#     100945,
#     95043,
#     105766,
#     121289]})
####################################################
df = pd.DataFrame({'cnt': [2318,
                           2228,
                           2981,
                           2121,
                           2037,
                           2329,
                           2559,
                           1659,
                           1924,
                           1468,
                           1847,
                           2207,
                           1152]})
####################################################
df = pd.DataFrame({'cnt': [3098,
                           2814,
                           2949,
                           2660,
                           2749,
                           2318,
                           2853,
                           2380,
                           2390,
                           2212,
                           2724,
                           2445,
                           2228,
                           2413,
                           2403,
                           2318,
                           2589,
                           2670,
                           2636,
                           2981,
                           2607,
                           2817,
                           2859,
                           2163,
                           2412,
                           2151,
                           2121,
                           2196,
                           2303,
                           2193,
                           3306,
                           2250,
                           2606,
                           2037,
                           2707,
                           2375,
                           2387,
                           2532,
                           2949,
                           2707,
                           2329,
                           2514,
                           2508,
                           2933,
                           2917,
                           3070,
                           2413,
                           2559,
                           3053,
                           2741,
                           2511,
                           2176,
                           2106,
                           1732,
                           1659,
                           1756,
                           1786,
                           1854,
                           1768,
                           2126,
                           2070,
                           1924,
                           2146,
                           2190,
                           1756,
                           1285,
                           1588,
                           1398,
                           1468,
                           1924,
                           1847,
                           1751,
                           1793,
                           2017,
                           1825,
                           1847,
                           2019,
                           2179,
                           1921,
                           1628,
                           1639,
                           1983,
                           2207,
                           2024,
                           1925,
                           2082,
                           2118,
                           2542,
                           2097,
                           1152]})

desc = df.cnt.describe()
print(desc)
# print(df.describe())
# print("-" * 60)
# desc = df.describe()
# print(desc.iloc[0])
# print(desc.loc['count'])
# print(desc.iloc[1])
# print(desc.loc['mean'])
# print(desc.iloc[2])
# print(desc.loc['std'])
# print(desc.iloc[3])
# print(desc.loc['min'])
# print(desc.iloc[4])
# print(desc.loc['mean'])
# print(desc.iloc[5])
# print(desc.loc['25%'])
# print(desc.iloc[6])


# print(desc.loc['75%'])
# print(desc.iloc[7])
# print(desc.loc['max'])

print("-" * 60)
_count = desc.loc['count']
_mean = desc.loc['mean']
_std = desc.loc['std']
_p25 = desc.loc['25%']
_p75 = desc.loc['75%']
_minimum = desc.loc['min']
_maximum = desc.loc['max']
print(_p25, _p75)


# c = 1.96
# delta = c * std / math.sqrt(count)
# print("%s = %d" % ('delta', delta))
# limitDF = pd.DataFrame({'low': mean - delta, 'high': mean + delta})
# print("%s is (%d, %d)" % ('limitDF', int(limitDF['low']), int(limitDF['high'])))
# print("-" * 60)


def gen_limit_frame(df, c):
    desc = df.describe()
    count = desc.loc['count']
    mean = desc.loc['mean']
    std = desc.loc['std']
    p25 = desc.loc['25%']
    p75 = desc.loc['75%']
    minimum = desc.loc['min']
    maximum = desc.loc['max']

    delta = c * std / math.sqrt(count)

    limitDF = pd.DataFrame({'low': mean - delta, 'high': mean + delta})
    return limitDF


print(gen_limit_frame(df, 1.96))

zScore = zscore(df)
df['zScore'] = zScore
print(df)


def lambda_exception_score(value, p25, p75):
    limit_basic = int((p75 - p25 + 500) * 1.5)
    print("value=%d, limit_basic=%d, p25=%d p75=%d" % (value, limit_basic, p25, p75))
    if value < p25:
        return (p25 - value) / limit_basic
    elif value > p75:
        return (value - p75) / limit_basic

    else:
        return 0.0


def lamb_exception_score(value):
    limit_basic = int((_p75 - _p25 + 100) * 1.5)
    # print("value=%d, limit_basic=%d, p25=%d p75=%d" % (value, limit_basic, _p25, _p75))
    if value < _p25:
        return (_p25 - value) / limit_basic
    elif value > _p75:
        return (value - _p75) / limit_basic

    else:
        return 0.0


print("-" * 60)
print(lambda_exception_score(3684, _p25, _p75))
print(lambda_exception_score(3911, _p25, _p75))
print(lambda_exception_score(3720, _p25, _p75))

print("-" * 60)
df['exScore'] = df['cnt'].map(lamb_exception_score)
df = df[df['exScore'] > 0.0]
df['zScore'] = df['zScore'].map(lambda x: abs(x))
print(df)
sns.jointplot(x="zScore", y="exScore", data=df)
plt.show()

# def calculate_exception_score(df, col_name, alfa, times):
#     desc = df.describe()
#     count = desc.loc['count']
#     mean = desc.loc['mean']
#     std = desc.loc['std']
#     p25 = desc.loc['25%']
#     p75 = desc.loc['75%']
#     minimum = desc.loc['min']
#     maximum = desc.loc['max']
#
#     limit_basic = int((p75 - p25 + 500) * 1.5)
#     print("value=%d, limit_basic=%d, p25=%d p75=%d" % (value, limit_basic, p25, p75))
#     if value < p25:
#         return (p25 - value) / limit_basic
#     elif value > p75:
#         return (value - p75) / limit_basic
#
#     else:
#         return 0.0
