# -*- coding: utf-8 -*-
#Time: 2018/8/23 22:28:37
#Description: 实现公钥登陆
#File Name: transport_public_key.py
import paramiko 
# 指定本地的RSA私钥文件,如果建立密钥对时设置的有密码，提供password参数即可，如无则不提供
pkey = paramiko.RSAKey.from_private_key_file('/home/aaron/.ssh/id_rsa')
#建立连接
transport = paramiko.Transport(('192.168.195.129',22))
transport.connect(username='aaron',pkey=pkey)
ssh = paramiko.SSHClient()
ssh._transport = transport

# 执行命令
stdin, stdout, stderr = ssh.exec_command('echo `date` && df -hl')
# 输出
print(stdout.read().decode('utf-8'))
# 关闭连接
transport.close()

