import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.163.com"
mail_user = "jamesqjiang"
mail_pass = "jamesqjiang"

sender = 'jamesqjiang@163.com'
receivers = ['jamesqjiang@163.com']

content = '我用Python'
title = 'send_email_with_excel'
csv_file_path = "/home/james/桌面/_CURRENT_WORK/_爬虫数据/shenzhen_201911202222.csv"
csv_file_name = "shenzhen_201911202222.csv"

msg = MIMEMultipart()
msg.attach(MIMEText("send_email_with_excel"))
msg['Subject'] = Header(title, 'utf-8')  # subject
# msg['From'] = sender
# msg['To'] = receivers

xlsx = MIMEText(open(csv_file_path, 'rb').read(), 'base64', 'utf-8')
xlsx["Content-Type"] = 'application/octet-stream'
xlsx.add_header('Content-Disposition', 'attachment', filename=csv_file_name)
msg.attach(xlsx)

# attachment = MIMEText(open(csv_file_path, 'rb').read(), 'base64', 'utf-8')
# attachment["Content-Type"] = 'application/octet-stream'
# # 生成附件的名称
# attachment[
#     "Content-Disposition"] = 'attachment; filename=' + csv_file_name
# # 将附件内容插入邮件中
# msg.attach(attachment)


smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
smtpObj.login(mail_user, mail_pass)  # 登录验证
smtpObj.sendmail(sender, receivers, msg.as_string())  # 发送
print("mail has been send successfully.")
