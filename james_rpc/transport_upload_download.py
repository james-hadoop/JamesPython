# -*- coding: utf-8 -*-
#Time: 2018/8/23 22:07:12
#Description: 实现上传和下载功能
#File Name: transport_upload_download.py
 
import paramiko

trans = paramiko.Transport(('192.168.195.129', 22))
# 建立连接,指定SSHClient的_transport
trans.connect(username='aaron', password='aaron')
ssh = paramiko.SSHClient()
ssh._transport = trans
# 执行命令，和传统方法一样
stdin, stdout, stderr = ssh.exec_command('echo `date` && df -hl')
print(stdout.read().decode('utf-8'))

# 实例化一个 sftp对象,指定连接的通道
sftp = paramiko.SFTPClient.from_transport(trans)
# 发送文件
sftp.put(localpath='./transport_upload_download.py',
        remotepath='/tmp/transport_upload_download_tmp.py')
# 下载文件
# sftp.get(localpath='./transport_upload_download.py',
#        remotepath='/tmp/transport_upload_download_tmp.py')
stdin, stdout, stderr = ssh.exec_command('ls -ltr /tmp')
print(stdout.read().decode('utf-8'))
# 关闭连接
trans.close()
