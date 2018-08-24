
'''
需求：

1. 要求将所有级别的所有日志都写入磁盘文件中
2. all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
3. err.log文件单独记录error及以上级别的日志信息，日志格式为： 日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
4 要求all.log在每天凌晨进行日志切割

分析：

1. 要记录所有级别的日志，因此日志器的有效level需要设置为最低级别-debug
2. 日志需要被发送到两个不同的目的地，因此需要为日志器设置两个handler，两个目的地都是磁盘文件，因此这两个handler都是与FileHandler
3. all.log要求按照时间进行日志分割，因此需要用logging.handler.TimeRotatingFileHandler;而error.log没有要求日志切割
4. 两个日志文件的格式不同，因此需要对这两个handler分别设置格式器
'''

import logging
import logging.handlers
import datetime

#定义logger
logger = logging.getLogger('log01')
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler('all.log',when='midnight',interval=1, backupCount=7)
rf_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s'))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug('我是debug')
logger.error('错误')