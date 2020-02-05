import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

N = 10000
x = np.random.normal(0, 1, N)
# ddof取值为1是因为在统计学中样本的标准偏差除的是(N-1)而不是N，统计学中的标准偏差除的是N
# SciPy中的std计算默认是采用统计学中标准差的计算方式
mean, std = x.mean(), x.std(ddof=1)
print(mean, std)
# 计算置信区间
# 这里的0.9是置信水平
conf_intveral = stats.norm.interval(0.95, loc=mean, scale=std)
print(conf_intveral)

# 绘制概率密度分布图
x = np.arange(-5, 5, 0.001)
# PDF是概率密度函数
y = stats.norm.pdf(x, loc=mean, scale=std)
plt.plot(x, y)
plt.show()
