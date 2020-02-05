from datetime import datetime, timedelta


# oneDayTimeOffset = timedelta(days=1)
# sevenDayTimeOffset = timedelta(days=7)
#
# statDate = 20200203
# statDateTime = datetime.strptime(str(statDate), '%Y%m%d')
#
# sevenDayBeforeStatDate = statDateTime - (oneDayTimeOffset * 7)
#
# sevenDayBeforeStatDate = int(sevenDayBeforeStatDate.strftime('%Y%m%d'))
#
# print("sevenDayBeforeStatDate=%d" % sevenDayBeforeStatDate)
# print("-" * 60)
#
# for i in range(0, 12):
#     dayOffset = sevenDayTimeOffset * i
#     statDay = statDateTime - dayOffset
#     statDay = int(statDay.strftime('%Y%m%d'))
#     print("statDay=%d" % statDay)
# print("-" * 60)


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


def main():
    statWeekDayList = make_stat_week_day_list(20200203, 1, 7, 16)
    print(statWeekDayList)
    print("-" * 60)

    statWeekDayList2 = make_stat_week_day_str_list('2020-02-03', 1, 7, 16)
    print(statWeekDayList2)


if __name__ == '__main__':
    main()
