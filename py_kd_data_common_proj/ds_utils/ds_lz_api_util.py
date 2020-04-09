# coding:utf-8
import logging as log
from datetime import datetime, timedelta

import requests


def make_lz_instance_status_url(task_id, task_time, task_type='d'):
    url = str('http://10.222.106.18/LService/QueryTaskRun?pageSize=24&task_id=')
    space = str('%20')
    zero4 = str('0000')
    zero_hour = str('%2000:00:00')
    day_instance_hour = '000000'

    day_hour_str = task_time
    day_str = str(day_hour_str)[0:8]
    hour_str = str(day_hour_str)[8:10]

    # param_day
    day_str = str(datetime.strptime(day_str, '%Y%m%d'))
    param_day = str(day_str).replace(" ", space)

    # param_start_hour, param_end_hour
    day_hour_offset = timedelta(hours=1)
    day_hour = datetime.strptime(day_hour_str, '%Y%m%d%H')
    end_hour = day_hour - day_hour_offset * 5
    start_hour = day_hour - day_hour_offset * 8
    param_start_hour = str(start_hour).replace(" ", space)
    param_end_hour = str(end_hour).replace(" ", space)
    # print(f'param_day={param_day}, param_start_hour={param_start_hour}, param_end_hour={param_end_hour}')
    log.info("param_day=%s, param_start_hour=%s, param_end_hour=%s" % (param_day, param_start_hour, param_end_hour))

    full_url = url + task_id + '&startTime=' + param_day + '&endTime=' + param_day
    if task_type == 'd':
        full_url = url + task_id + '&startTime=' + param_day + '&endTime=' + param_day

    elif task_type == 'h':
        full_url = url + task_id + '&startTime=' + param_start_hour + '&endTime=' + param_end_hour

    log.info("full_url=%s" % full_url)
    return full_url


def get_task_status(full_url):
    task_status = 'NULL'
    r = 'NULL'

    try:
        r = requests.get(url=full_url)
        # print(r.json())

        if r.json()[0]['state'] == 'success':
            task_status = r.json()[0]['desc'].encode('utf-8')

        return task_status
    except Exception as e:
        log.error('failed get http response from LZ!!!')
        return task_status
