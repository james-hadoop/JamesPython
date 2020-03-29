import time
import datetime
import subprocess
import functools
import os


def fetch_all(COR, sql):  # wrapper for sql
    COR.execute(sql)
    return COR.fetchall()


def execute_sql(COR, CON, sql):
    COR.execute(sql)
    CON.commit()


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


def map1(lam, *args):  # functional programming
    return list(map(lam, *args))


def filter1(lam, *args):  # functional programming
    return list(filter(lam, *args))


def reduce1(f, _list):  # functional programming
    return functools.reduce(f, _list)


def mkdir_if_not_exist(_dir):
    if not os.path.exists(_dir):
        os.makedirs(_dir)


def execute_cmd(cmd):
    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    stdout, stderr = p.communicate()
    return stdout, stderr


def is_digit(s):
    s = str(s)
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()
