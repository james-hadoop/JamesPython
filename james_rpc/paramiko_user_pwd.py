# -*- coding: utf-8 -*-
# File Name: paramiko_user_pwd.py
# Description: 使用用户名密码来登陆并执行远程命令
import paramiko

# 建立一个sshclient对象
ssh = paramiko.SSHClient()
# 将信任的主机自动加入到host_allow列表，须放在connect方法前面
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 调用connect方法连接服务器
ssh.connect(hostname="192.168.195.129", port=22, username="aaron", password="aaron")
# 执行命令
stdin, stdout, stderr = ssh.exec_command("echo `date` && df -hl")
# 结果放到stdout中，如果有错误将放到stderr中
print(stdout.read().decode('utf-8'))
# 
returncode = stdout.channel.recv_exit_status()
print("returncode:",returncode)
# 关闭连接
ssh.close()
