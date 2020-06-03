#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import statsmodels.api as sm
import sys
import numpy as np


#dat = pd.read_csv('kb_hurdle.csv')
dat = pd.read_csv('/Users/qjiang/workspace4py/JamesPython/james_tct/_data/kb2.csv')
#把所有为\\N的字段置为0
dat.replace('\\N', 0, inplace=True)
#dat.cur_app_min[dat.cur_app_min == '\\N'] = 0

#print(dat.columns)
cols=dat.columns[4:]
#print(cols)
#把不是中文的指标字段转成float类型
for col in cols[:]:
    dat[col] = np.array(dat[col],dtype=float)

#对一些分布非常广的变量X取log对数
print(cols[30:36])
for col in cols[30:36]:
    dat[col] = np.log(dat[col] + 1)
print(cols[37:43])
for col in cols[37:43]:
    dat[col] = np.log(dat[col] + 1)


# In[6]:


print(cols)


# In[135]:




import math
import numpy as np
#dat = dat[np.ceil(dat.cur_app_min) > 0]

#过滤掉视频消费时长小于0的样本，从20万下降到7万
dat = dat[dat.cur_app_min > 0]

#对y取log对数，使其符合Gamma分布
#dat.cur_app_min = np.log(dat.cur_app_min + 1)

#对视频消费时长取floor，让其符合泊松分布
#dat.cur_app_min = np.floor(dat.cur_app_min)

#print(dat.shape)

# model = sm.formula.glm("cur_app_min ~ cur_likes+ cur_dislikes+ cur_comments+cur_shares+ cur_fuli_main_expo+ cur_refr+ cur_refr_tl+ cur_launch_times+ cur_fuli_coin+ cur_sp_tags+cur_tw_tags+ cur_tw_exp+ cur_sp_exp+ cur_tw_exp_avg_hot_ratio+cur_tw_avg_pic_resolution+ cur_sp_avg_resolution+cur_tw_exp_avg_high_quality+ cur_tw_exp_avg_cover_attract+ cur_tw_avg_words_num+ cur_tw_exp_cat1s+cur_exp_ratio_tw_human+ cur_exp_ratio_tw_feedback+cur_pv_ratio_interest+ cur_sp_avg_cover_pic_resolution+cur_push_receive_pv+ cur_push_click_pv",
#                         family=sm.families.Poisson(), data=dat).fit()

# model = sm.formula.glm("cur_app_min ~ cur_likes+ cur_dislikes+ cur_comments+cur_shares+ cur_fuli_main_expo+ cur_refr+ cur_refr_tl+ cur_launch_times+ cur_fuli_coin+ cur_sp_tags+cur_tw_tags+ cur_tw_exp+ cur_sp_exp+ cur_tw_exp_avg_hot_ratio+cur_tw_avg_pic_resolution+ cur_sp_avg_resolution+cur_tw_exp_avg_high_quality+ cur_tw_exp_avg_cover_attract+ cur_tw_avg_words_num+ cur_tw_exp_cat1s+cur_exp_ratio_tw_human+ cur_exp_ratio_tw_feedback+cur_pv_ratio_interest+ cur_sp_avg_cover_pic_resolution+cur_push_receive_pv+ cur_push_click_pv",
#                         family=sm.families.Gamma(), data=dat).fit()
# + ++ + + 
# ++ +
# + + + 
# ++ ++ 
# ++ 
model = sm.formula.glm("cur_app_min ~ cur_push_click_pv",
                        family=sm.families.Gamma(), data=dat).fit()
#print(model.summary())
print(model.summary2())
# with open('count.txt','w+') as f:
#     print(model.summary2(), file=f)


# In[136]:


nobs = model.nobs
#y = dat.cur_app_min/dat.cur_app_min.sum()
#y = dat.cur_app_min
y = np.log(dat.cur_app_min + 1) / (np.log(dat.cur_app_min + 1)).sum()
print(y.shape)
yhat = model.mu
#yhat = np.exp(yhat) - 1
print(yhat.shape)


# In[137]:


from statsmodels.graphics.api import abline_plot
from matplotlib import pyplot as plt
import seaborn as sns


# In[138]:


#sns.regplot('cur_shares', 'cur_app_min', dat)
#sns.regplot(dat.cur_sp_avg_resolution, model.mu)
sns.regplot(dat.cur_push_click_pv, model.fittedvalues)
#sns.despine(offset=10);


# # In[39]:
#
#
# sns.regplot(dat.cur_shares, dat.cur_app_min)
#
#
# # In[29]:
#
#
# fig, ax = plt.subplots(figsize=(8,6))
# ax.plot(dat.cur_shares, dat.cur_app_min, 'o', label='data')
# ax.plot(dat.cur_shares, yhat, 'r--.',label='OLS')
# # ax.scatter(yhat, y)
# # line_fit = sm.OLS(y, sm.add_constant(yhat, prepend=True)).fit()
# # abline_plot(model_results=line_fit, ax=ax)
#
#
# ax.set_title('Model Fit Plot')
# ax.set_ylabel('Observed values')
# ax.set_xlabel('Fitted values');
#
#
# # In[ ]:




