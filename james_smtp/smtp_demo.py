import smtplib

HOST = 'smtp@163.com'
SUBJECT = u'测试'
TO = 'sysinfo@yuanqucha.com'
FROM = 'jamesqjiang@163.com'
text = u'测试邮件'
BODY = "\r\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
))

print(BODY)

server = smtplib.SMTP()
server.connect(HOST, "25")
server.starttls()
server.login("jamesqjiang@163.com", "james123")
server.sendmail(FROM, [TO], BODY)
server.quit()
