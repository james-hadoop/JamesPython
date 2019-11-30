import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.163.com"
mail_user = "jamesqjiang"
mail_pass = "jamesqjiang"

sender = 'jamesqjiang@163.com'
receivers = ['jamesqjiang@163.com']

content = '我用Python'
title = "chengxuyuan"

img_file_path = "/home/james/图片/pic/yidian_1181029123520.jpg"

msg = MIMEMultipart('related')
msgtext = MIMEText("<font color=red>程序猿:<br><img src=\"cid:chengxuyuan\" border=\"1\"><br>详细内容见附件。</font>", "html",
                   "utf-8")


def addimg(src, imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage


msg.attach(msgtext)
msg.attach(addimg(img_file_path, title))

msg['Subject'] = Header(title, 'utf-8')  # subject
msg['From'] = sender
msg['To'] = receivers

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
    smtpObj.login(mail_user, mail_pass)  # 登录验证
    smtpObj.sendmail(sender, receivers, msg.as_string())  # 发送
    print("mail has been send successfully.")
except smtplib.SMTPException as e:
    print(e)
