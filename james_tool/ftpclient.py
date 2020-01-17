# -*- encoding:utf-8 -*-
from ftplib import FTP
#登陆FTP
ftp = FTP(host='localhost',user='user',passwd='12345')
#设置编码方式，由于在windows系统，设置编码为gbk
ftp.encoding = 'gbk'
# 切换目录
ftp.cwd('test')
#列出文件夹的内容
ftp.retrlines('LIST') # ftp.dir()
#下载文件 note.txt
ftp.retrbinary('RETR note.txt', open('note.txt', 'wb').write)
#上传文件 ftpserver.py
ftp.storbinary('STOR ftpserver.py', open('ftpserver.py', 'rb'))
#查看目录下的文件详情
for f in ftp.mlsd(path='/test'):
    print(f)