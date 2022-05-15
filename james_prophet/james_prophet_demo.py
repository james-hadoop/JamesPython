import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 模型训练prophet
from fbprophet import Prophet  # 导入模型

plt.rcParams['axes.unicode_minus'] = False  # 这句代码解决待会画图出来  坐标轴负号乱码问题

# 数据加载
data = pd.read_csv(
    '/home/james/_AllDocMap/05_Dateset/Purchase-Redemption-Data/user_balance_table.csv')
# user_id就是用户 report_date是日期 tBalance是今日余额  yBalance是昨日余额  total_purchase_amt 今日总购买量（=直接购买+收益）
# direct_purchase_amt是直接购买  purchase_bal_amt今日支付宝余额购买量  purchase_bank_amt今日银行卡购买量
# total_redeem_amt今日总赎回量（=消费+转出） consume_amt今日总消费量 transfer_amt今日转出总量
# tftobal_amt今日转出到支付宝余额总量 tftocard_amt今日转出到银行卡总量   share_amt今日收益
# category1 category2 category3 category4分别表示类目1 2 3 4 消费总额
# 其中 total_purchase_amt 和 total_redeem_amt 是我们要预测的目标值

# 2840421个数据里面 时间只有427个  时间最早是从2013-07-01  最晚是到2018-31-31
# data = data.sort_index(axis=0, by='input_date', ascending=True)
# subset = subset.sort_values(axis=0, by=['s_cont_stat_date', 'union_chann_id'], ascending=True)
data['report_date'].value_counts().sort_index()

data.info()  # 'report_date'这个字段的类型是datetime64[ns]  其他的都是整形和浮点型

# 这个时候可以根据时间来做一个分组聚合操作
# data = data.groupby(['union_chann_id', 's_cont_stat_date'])['today_ruku_cont_cnt'].sum()
total_balance = data.groupby(['report_date'])['total_purchase_amt', 'total_redeem_amt'].sum()
total_balance  # 这里果然是427行  然后对应的天数 total_purchase_amt求和了  total_redeem_amt也求和了

purchase = total_balance[['total_purchase_amt']]
purchase  # 这样就有了一个新的dataframe 专门存储 某天的购买  这个也是我们要预测的这一列

redeem = total_balance[['total_redeem_amt']]
redeem  # 这个dataframe专门存储赎回 也就是当天的赎回（消费+转出）  这个也是我们要预测的一列


# 指定区间范围内的数据,进行可视化
def plot_stl(data):
    # STL返回三个部分：trend(趋势),seasonal(季节),residual(残差)
    result = sm.tsa.seasonal_decompose(data, period=30)  # 我们的数据量只有从2013-07-01到2014-08-31一年多的数据量 而且我们要预测的仅仅是下一个月
    # 所以这里的参数period=30 算是一个周期      如果像股票那样周期是年的  可以设置成200
    # 可视化
    fig = plt.figure(figsize=(12, 8))
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)
    # result里面包含三个部分 trend(趋势),seasonal(季节),residual(残差)
    result.trend.plot(ax=ax1, title='Trend趋势')
    result.seasonal.plot(ax=ax2, title='Seasonal季节')
    result.resid.plot(ax=ax3, title='Resid残差')

    plt.show()


plot_stl(purchase['total_purchase_amt'])  # 这里三张图的横坐标都是表格中的日期类型  从2013年7月到2014年8月

plot_stl(redeem['total_redeem_amt'])

# 上面的 那个 purchase 中的字段 total_purchase_amt 今日总购买量 是我们要预测的一列
# prophet模型里面有个保留字 ‘ds’
purchase['ds'] = purchase.index
purchase.rename(columns={'total_purchase_amt': 'y'}, inplace=True)  # 给字段改个名字 把 total_purchase_amt 换成y
purchase  # 同时把那个时间给了保留字 ds

redeem['ds'] = redeem.index  # 同理也把这里的ds也给复制一下 prophet的保留字
redeem.rename(columns={'total_redeem_amt': 'y'}, inplace=True)  # 同时也给这个名字要预测的字段  redeem 总赎回量(消费+转出) 也给更改一下名字
redeem

# 这个时候再把purchase redeem的索引给重新更改一下
purchase = purchase.reset_index(drop=True)
purchase  # 这样就把索引给还原了   同样可以做一下redeem的

redeem = redeem.reset_index(drop=True)
redeem  # 这样就把索引给还原了   同样可以做一下redeem的

# 构造Prophet模型  weekly_seasonality=True表示周期为周的季节性 n_changepoints=300指定突变点的个数
model = Prophet(weekly_seasonality=True, seasonality_prior_scale=0.1, n_changepoints=100)
model.fit(purchase)  # 训练拟合模型  这里是购买的那个数据 purchase

# 预测未来1个月，9月份30天
future = model.make_future_dataframe(periods=30)
purchase_pred = model.predict(future)
purchase_pred  # propeht预测出来的是一个区间 这里下面有很多的参数  #这里是457行 因为原本的数据是427行数据  然后按照时序模型再预测了30天

_ = model.plot(purchase_pred) # 可视化一下 黑点是实际的点  蓝色的是我们预测出来的  感觉不是很准太平缓了
plt.show()
# plot方法会返回一个figure对象  如果不用一个变量接一下  这个图就显示两边

# 同样可以做一下 redeem的拟合和预测
model2 = Prophet(weekly_seasonality=True, seasonality_prior_scale=0.1, n_changepoints=100)
model2.fit(redeem)
# 预测未来1个月，9月份30天
future = model2.make_future_dataframe(periods=30)
redeem_pred = model2.predict(future)
redeem_pred

_ = model2.plot(redeem_pred)
plt.show()

# 预测结果有了 然后筛选一下  作为结果输出  这个是总购买量的预测 预测指定的时间 就是下一个月
purchase_pred[(purchase_pred['ds'] >= '2014-09-01') & (purchase_pred['ds'] <= '2014-09-30')]

# 用一个结果存储一下
purchase2 = purchase_pred[(purchase_pred['ds'] >= '2014-09-01') & (purchase_pred['ds'] <= '2014-09-30')][
    ['ds', 'yhat']]  # ds是时间列 yhat是预测值
purchase2  # 这个是总购买量

redeem2 = redeem_pred[(redeem_pred['ds'] >= '2014-09-01') & (redeem_pred['ds'] <= '2014-09-30')][['ds', 'yhat']]
redeem2  # z这个是总赎回量

# 合并拼接结果
result = pd.DataFrame()  # 一个空的df
result['ds'] = purchase2['ds']  # 然后把时间放进去
result['purchase_amt'] = purchase2['yhat']  # 把总购买量放进去
result['redeem_amt'] = redeem2['yhat']  # 把总赎回量放进去
result

result.to_csv('n_prophet_python.csv', header=None, index=False)  # 这样直接提交结果是不正确的 因为不符合题目的要求 要把日期中间的'-'给去掉

result['ds'] = result['ds'].apply(lambda x: str(x).replace('-', ''))
result
# result#这样做 后面的0000000都显示出来了  不需要  所以只需要前8位

result['ds'] = result['ds'].apply(lambda x: str(x).replace('-', '')[0:8])
result  # 这样做 后面的0000000都显示出来了  不需要  所以只需要前8位

result.to_csv('n_prophet_python.csv', header=None, index=False)
