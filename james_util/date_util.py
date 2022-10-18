from datetime import datetime, timedelta


def make_stat_week_day_list(stat_date, plus_minus, offset, count):
    statWeekDayList = []
    sevenDayTimeOffset = timedelta(days=offset)

    statDateTime = datetime.strptime(str(stat_date), '%Y%m%d')
    for i in range(0, count):
        dayOffset = sevenDayTimeOffset * i
        statDay = statDateTime + (dayOffset * plus_minus)
        statDay = int(statDay.strftime('%Y%m%d'))
        statWeekDayList.append(statDay)

    return statWeekDayList


def make_stat_week_day_str_list(stat_date, plus_minus, offset, count):
    statWeekDayList = []
    sevenDayTimeOffset = timedelta(days=offset)

    statDateTime = datetime.strptime(str(stat_date), '%Y-%m-%d')
    for i in range(0, count):
        dayOffset = sevenDayTimeOffset * i
        statDay = statDateTime + (dayOffset * plus_minus)
        statDay = str(statDay.strftime('%Y-%m-%d'))
        statWeekDayList.append(statDay)

    return statWeekDayList


def make_stat_week_day_list(stat_date, plus_minus, offset, count, date_format='%Y-%m-%d'):
    statWeekDayList = []
    sevenDayTimeOffset = timedelta(days=offset)

    statDateTime = datetime.strptime(str(stat_date), date_format)
    for i in range(0, count):
        dayOffset = sevenDayTimeOffset * i
        statDay = statDateTime + (dayOffset * plus_minus)
        statDay = str(statDay.strftime(date_format))
        statWeekDayList.append(statDay)

    return statWeekDayList
