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
receivers = ['sysinfo@yuanqucha.com']

content = u'请查收最新的园区政策信息'
title = '园区政策信息_20191223'

csv_file_path = "/Users/qjiang/Desktop/_CURRNET_WORK/_爬虫/yqc_spider_20191223.csv"
csv_file_name = "yqc_spider_20191223.csv"

msg = MIMEMultipart()
msg.attach(MIMEText('尊敬的先生/女士：  请查收最新的园区政策信息，感谢您的订阅！'))
msg['Subject'] = title  # subject
msg['From'] = 'jamesqjiang@163.com'
msg['To'] = 'sysinfo@yuanqucha.com'

xlsx = MIMEText(open(csv_file_path, 'rb').read(), 'base64', 'gb2312')
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


