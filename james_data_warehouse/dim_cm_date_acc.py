#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import datetime
import calendar
import lunardate
import csv

holiday_dict = {}

week_day_en_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                    4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

week_day_cn_dict = {1: '周一', 2: '周二', 3: '周三',
                    4: '周四', 5: '周五', 6: '周六', 7: '周日'}

month_cn_dict = {1: '一月', 2: '二月', 3: '三月',
                 4: '四月', 5: '五月', 6: '六月', 7: '7月', 8: '8月', 9: '9月', 10: '10月', 11: '11月', 12: '12月'}


# 判断二月闰月
def isLeapYear(year):
    return calendar.monthrange(year, 2)[1] == 29


# 季度信息
def quarter(month):
    return (month - 1) / 3 + 1


# 周信息
def get_week_of_year(dt):
    return dt.isocalendar()[1]


def get_week_of_month(dt):
    return dt.isocalendar()[0]


def get_day_of_year(dt):
    return dt.timetuple().tm_yday


def get_day_of_week(day):
    return day.weekday() + 1 % 7


# 返回是否最后一天
def last_day_of_month(year, month, day):
    if day == calendar.monthrange(year, month)[1]:
        return 1
    return 0


def get_is_weekend(day):
    return day.weekday() == 5 or day.weekday() == 6


# def get_holiday_dict(year, month):
#     params = {
#         'resource_id': 6018,
#         'ie': 'utf8',
#         'oe': 'utf8',
#         'format': 'json',
#         'tn': 'baidu'
#     }
#     query_arg = "%d年%d月"
#     params['query'] = query_arg % (year, month)
#     res = requests.get(url='https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?', params=params).text
#     # 取括号内的
#     res = res[res.find("{"): res.rfind("}") + 1]
#
#     js = json.loads(res, encoding='utf-8')
#
#     holiday_list = js.get('data')[0].get('holiday')
#
#     for i in holiday_list:
#         list_list = i.get('list')
#         name = i.get('name')
#         day_cnt = len(list_list)
#         for x in list_list:
#             status = x.get('status')
#             if status == 2:
#                 day_cnt -= 1
#
#         for j in list_list:
#             dt = j.get('date')
#             status = j.get('status')
#             item_info = (status, name, day_cnt)
#             holiday_dict[dt] = item_info


# 获取阴历日期
def get_lunar_dt(dt):
    ymd = dt.split('-')
    lunar = lunardate.LunarDate.fromSolarDate(int(ymd[0]), int(ymd[1]), int(ymd[2]))
    return "%d-%02d-%02d" % (lunar.year, lunar.month, lunar.day_cur)


def get_is_holiday(day):
    dt = day.strftime("%Y-%-m-%-d")
    item = holiday_dict.get(dt)
    if item is not None:
        return int(item[0]) == 1
    else:
        return False


def is_work_day(day, is_weekend):
    dt = day.strftime("%Y-%-m-%-d")
    item = holiday_dict.get(dt)
    if item is not None:
        # 如果在holiday列表里但是状态等于2
        return int(item[0]) == 2
    else:
        return not (is_weekend)


def get_holiday_cnt(day):
    dt = day.strftime("%Y-%-m-%-d")
    item = holiday_dict.get(dt)
    if item is not None and int(item[0]) == 1:
        return int(item[2])
    else:
        return 0


def get_holiday_type(day, is_weekend):
    dt = day.strftime("%Y-%-m-%-d")
    item = holiday_dict.get(dt)
    if item is not None:
        if int(item[0]) == 1:
            if str(item[1]) == '元旦':
                return 3
            elif str(item[1]) == '春节':
                return 4
            elif str(item[1]) == '清明节':
                return 5
            elif str(item[1]) == '劳动节':
                return 6
            elif str(item[1]) == '端午节':
                return 7
            elif str(item[1]) == '中秋节':
                return 8
            elif str(item[1]) == '国庆节':
                return 9
            else:
                return 99
        else:
            return 1

    else:
        if is_weekend:
            return 2
        else:
            return 1
    return 1


def write_csv(data_row):
    path = "/Users/jiangqian/Documents/_AllDocMap/02_Project/ws4python/JamesPython/_data/dim_cm_date_acc.csv"
    with open(path, 'a+') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data_row)


if __name__ == '__main__':
    # 开始日期
    start_date = datetime.datetime(2020, 1, 1)
    # 结束日期
    end_date = datetime.datetime(2024, 12, 31)
    # 当天
    day_cur = start_date

    while day_cur <= end_date:
        data_date = day_cur.strftime("%Y-%m-%d")
        dt = int(day_cur.strftime('%Y%m%d'))
        # 当月第一天
        one_time = day_cur.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        calendar_year = day_cur.year

        '''
          data_date string comment '日期，格式：yyyy-MM-dd',
          day_of_week string comment '周几，枚举：Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday',
          day_of_month int comment '本月第几天',
          day_of_year int comment '本年第几天',
          week_of_month int comment '本月第几周',
          week_of_year int comment '本年第几周',
          month string comment '月份，枚举：Jan｜Feb｜Mar｜Apr｜May｜Jun｜Jul｜Aug｜Sept｜Oct｜Nov|Dec',
          year int comment '年份，格式：yyyy'
        '''

        day_of_week_key = get_day_of_week(day_cur)
        day_of_week = week_day_cn_dict[day_of_week_key]

        day_of_month = day_cur.day
        day_of_year = get_day_of_year(day_cur)

        week_of_month = int(day_cur.strftime('%W')) - int(one_time.strftime('%W')) + 1
        week_of_year = get_week_of_year(day_cur)

        month_of_year_key = day_cur.month
        month = month_cn_dict[month_of_year_key]
        quarter_of_year = quarter(day_cur.month)

        is_last_day_of_month = last_day_of_month(calendar_year, month_of_year_key, day_of_month)
        is_weekend = get_is_weekend(day_cur)

        year = day_cur.year
        # is_holiday = get_is_holiday(day)
        # holiday_type = get_holiday_type(day, is_weekend)
        # holiday_cnt = get_holiday_cnt(day)

        data_raw = [dt, data_date, day_of_week, day_of_month, day_of_year, week_of_month, week_of_year, month,
                    is_last_day_of_month, year]
        print(data_raw)

        write_csv(data_raw)

        day_cur = day_cur + datetime.timedelta(days=1)
