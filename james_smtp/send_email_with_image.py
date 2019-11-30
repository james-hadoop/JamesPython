import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# 第三方 SMTP 服务
mail_host = "smtp.163.com"
mail_user = "jamesqjiang"
mail_pass = "jamesqjiang"

sender = 'jamesqjiang@163.com'
receivers = ['jamesqjiang@163.com']

content = '我用Python'
title = 'send_email_with_attach'


def addimg(src, imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage


msg = MIMEMultipart('related')
msgtext = MIMEText("<font color=red>程序猿:<br><img src=\"cid:chengxuyuan\" border=\"1\"><br>详细内容见附件。</font>", "html",
                   "utf-8")
msg.attach(msgtext)
msg.attach(addimg("/home/james/图片/pic/yidian_1181029123520.jpg", "chengxuyuan"))


def sendEmail():
    global msg
    msgtext = MIMEText("<font color=red>程序猿:<br><img src=\"cid:chengxuyuan\" border=\"1\"><br>详细内容见附件。</font>", "html",
                       "utf-8")
    # msg.attach(msgtext)
    msg.attach(addimg("/home/james/图片/pic/yidian_1181029123520.jpg", "chengxuyuan"))
    msg['Subject'] = Header('send_email_with_image', 'utf-8')  # subject
    msg['From'] = sender
    msg['To'] = receivers

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
    smtpObj.login(mail_user, mail_pass)  # 登录验证
    smtpObj.sendmail(sender, receivers, msg.as_string())  # 发送
    print("mail has been send successfully.")
except smtplib.SMTPException as e:
    print(e)


def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    # email_client = smtplib.SMTP(SMTP_host)
    email_client = smtplib.SMTP_SSL(SMTP_host, 465)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()


if __name__ == '__main__':
    sendEmail()

    # send_email2(mail_host, 'jamesqjiang@163.com', mail_pass, 'jamesqjiang@163.com', title, content)
