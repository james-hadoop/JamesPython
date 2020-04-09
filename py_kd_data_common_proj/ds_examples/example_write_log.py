# 根据配置参数文件指定的日志路径，打日志。
# 日志默认级别是log.INFO，日志信息如下：
#
# 2020-04-01 17:28:27 example_write_log.py [line:27]     INFO: log info
# 2020-04-01 17:28:27 example_write_log.py [line:28]  WARNING: log warning
# 2020-04-01 17:28:27 example_write_log.py [line:29]    ERROR: log error
# 2020-04-01 17:28:27 example_write_log.py [line:30] CRITICAL: log critical
import datetime
import os

import configobj
import logging as log

config_path = os.getcwd() + '/../ds_conf/config.conf'
CO = configobj.ConfigObj(config_path)


def initLogConfig():
    LOG_DIR = CO['LOG']['log_dir']
    LOG_FILE = os.path.basename(__file__).split('.')[0]
    LOG_TIME = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    LOG_FULL_PATH = LOG_DIR + LOG_FILE + LOG_TIME + ".log"

    print("LOG_FULL_PATH=%s" % LOG_FULL_PATH)
    log.basicConfig(filename=LOG_FULL_PATH,
                    level=log.INFO, format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)8s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def main():
    initLogConfig()

    log.debug("log debug")
    log.info("log info")
    log.warning("log warning")
    log.error("log error")
    log.critical("log critical")


if __name__ == '__main__':
    main()
