import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)

x = np.random.normal(size=100)
# 绘制直方图.kde即kernel density estimate，用于控制是否绘制核密度估计
sns.distplot(x, kde=True)
plt.show()

mean, cov = [0, 3], [(1, .5), (.5, 1)]
# mean是多维分布的均值；cov是协方差矩阵。注意：协方差矩阵必须是对称的且需为半正定矩阵；
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])
# 创建密度图
sns.jointplot(x="x", y="y", data=df)
plt.show()
