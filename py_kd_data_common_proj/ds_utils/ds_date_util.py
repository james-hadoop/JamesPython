import math
from datetime import datetime, timedelta


def get_now(pattern="%Y%m%d"):
    now = datetime.datetime.now()
    return now.strftime(pattern)


def make_stat_week_day_list(stat_date, plus_minus, offset, count, pattern='%Y-%m-%d'):
    """
    @author jamesqjiang
    根据当前日期stat_date，生成count个，步长为offset的日期列表。plus_minus为正整数，则返回stat_date未来的日期列表；
    plus_minus为负整数，则返回stat_date过去的日期列表。
    :param stat_date: 当前日期，日期的格式需要与pattern一致
    :param plus_minus: 正整数表示当前日期未来的日期，负整数表示当前日期过去的日期
    :param offset: 步长，每个offset天，将这个日期添加到返回日期列表中
    :param count: 返回日期列表的最大元素个数
    :param pattern: 日期格式
    :return: 日期列表
    """
    statWeekDayList = []
    daysOffset = timedelta(days=offset)

    statDateTime = datetime.strptime(str(stat_date), pattern)
    for i in range(0, count):
        dayOffset = daysOffset * i
        statDay = statDateTime + (dayOffset * (plus_minus / math.fabs(plus_minus)))
        statDay = str(statDay.strftime(pattern))
        statWeekDayList.append(statDay)

    return statWeekDayList
