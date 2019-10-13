import logging

logger = logging.getLogger()

logger.setLevel(level=logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('logging_demo2.log', encoding='utf-8')

# 创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s')

fh.setFormatter(formatter)

ch.setFormatter(formatter)

logger.addHandler(fh)

logger.addHandler(ch)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
