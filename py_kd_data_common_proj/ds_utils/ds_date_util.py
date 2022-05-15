import math
from datetime import datetime, timedelta, time


def get_now(pattern="%Y%m%d"):
    now = datetime.datetime.now()
    return now.strftime(pattern)


def format_date(date, old_pattern="%Y-%m-%d %H:%M:%S", new_pattern="%Y%m%d"):
    formatted_date = datetime.strptime(str(date), old_pattern)
    formatted_date = str(formatted_date.strftime(new_pattern))

    return formatted_date


def unix_to_date(ts, pattern='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.fromtimestamp(ts).strftime(pattern)


def get_now_unix():
    return int(time.time())


def get_now(pattern="%Y%m%d"):
    time = datetime.datetime.now()
    return time.strftime(pattern)


def get_date(today, offset, pattern_from="%Y-%m-%d %H:%M:%S", pattern_to='%Y-%m-%d %H:%M:%S',
             granularity='day'):
    today_date = datetime.datetime.strptime(today, pattern_from)  # "%Y%m%d")
    tomorrow_date = today_date + datetime.timedelta(**{granularity + 's': int(offset)})
    return tomorrow_date.strftime(pattern_to)


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
    stat_week_day_list = []
    days_offset = timedelta(days=offset)

    stat_date_time = datetime.strptime(str(stat_date), pattern)
    for i in range(0, count):
        day_offset = days_offset * i
        stat_day = stat_date_time + (day_offset * (plus_minus / math.fabs(plus_minus)))
        stat_day = str(stat_day.strftime(pattern))
        stat_week_day_list.append(stat_day)

    return stat_week_day_list


# tpep_pickup_datetime         2020-12-01 10:11:41
# tpep_dropoff_datetime        2020-12-01 10:20:01
def delta_time(time_begin, time_end, time_begin_pattern='%Y-%m-%d %H:%M:%S', time_end_pattern='%Y-%m-%d %H:%M:%S'):
    time_delta = datetime.strptime(str(time_end), time_end_pattern) - datetime.strptime(str(time_begin),
                                                                                        time_begin_pattern)

    return time_delta


def main():
    # 格式化日期
    # date = '2020-01-01 00:28:15'
    # formatted_date = format_date(date, old_pattern="%Y-%m-%d %H:%M:%S")
    # print(formatted_date)

    time_begin = "2020-12-01 10:20:01"
    time_end = "2020-12-01 10:11:41"

    time_delta = delta_time(time_end, time_begin)

    print(f"time_delta={time_delta}")


if __name__ == '__main__':
    main()
