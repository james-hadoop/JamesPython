from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler,ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.log import LogFormatter
import logging


#记录日志，默认情况下日志仅输出到屏幕（终端），这里即输出到屏幕又输出到文件，方便日志查看
logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename='myftpserver.log',encoding='utf-8') #默认的方式是追加到文件
ch.setFormatter(LogFormatter())
fh.setFormatter(LogFormatter())
logger.addHandler(ch) #将日志输出至屏幕
logger.addHandler(fh) #将日志输出至文件


# 实例化虚拟用户，这是FTP验证首要条件
authorizer = DummyAuthorizer()
# 添加用户权限和路径，括号内的参数是(用户名， 密码， 用户目录， 权限),可以为不同的用户添加不同的目录和权限
authorizer.add_user("user", "12345", "d:/", perm="elradfmw")
# 添加匿名用户 只需要路径
authorizer.add_anonymous("d:/")

# 初始化ftp句柄
handler = FTPHandler
handler.authorizer = authorizer

#添加被动端口范围
handler.passive_ports = range(2000, 2333)

# 下载上传速度设置
dtp_handler = ThrottledDTPHandler
dtp_handler.read_limit = 300 * 1024 #300kb/s
dtp_handler.write_limit = 300 * 1024 #300kb/s
handler.dtp_handler = dtp_handler

# 监听ip 和 端口,linux里需要root用户才能使用21端口
server = FTPServer(("0.0.0.0", 21), handler)

# 最大连接数
server.max_cons = 150
server.max_cons_per_ip = 15

# 开始服务，自带日志打印信息
server.serve_forever()