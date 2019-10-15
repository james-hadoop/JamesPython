import smtplib

HOST = 'smtp@163.com'
SUBJECT = 'James SMTP Demo'
TO = 'jamesqjiang@163.com'
FROM = 'jamesqjiang@163.com'
text = 'Python rules them all!'
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
