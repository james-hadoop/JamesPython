import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 颜色设置
sns.palplot(sns.color_palette('hls', 14))

# 颜色亮度与饱和度
# sns.palplot(sns.hls_palette(8, l=0.3, s=0.8))

# 颜色分对
# sns.palplot(sns.hls_palette("Paired", 10))

# 颜色设置盒图
data = np.random.normal(size=(20, 8)) + np.arange(8) / 2
sns.boxplot(data=data, palette=sns.color_palette('hls', 8))

# 连续颜色
sns.palplot(sns.color_palette("Blues"))
sns.palplot(sns.color_palette("Blues_r"))

# 颜色深浅
sns.palplot(sns.light_palette('green'))
sns.palplot(sns.dark_palette('purple', reverse=True))

plt.show()
