# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "somezz"  # 用户名
mail_pass = "wqzz2123"  # 口令


sender = "somezz@163.com"
receivers = ["somenzz@qq.com", "zhengzheng@wjrcb.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText("这是正文：邮件正文......", "plain", "utf-8")  # 构造正文
message["From"] = sender  # 发件人，必须构造，也可以使用Header构造
message["To"] = ";".join(receivers)  # 收件人列表，不是必须的
message["Subject"] = "这是主题：SMTP 邮件测试"

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("发送成功")
except smtplib.SMTPException as e:
    print(f"发送失败,错误原因：{e}")
