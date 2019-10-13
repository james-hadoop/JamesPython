import logging

## 设置日志显示级别以及日志文件
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='logging_demo.log',
                    filemode='w')

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
