
import urllib,urllib2
url='http://localhost:8088/v1/service/user/getVerifyCode?hUserPhoneNr=15821615886'
req = urllib2.Request(url)
res = urllib2.urlopen(req)
res = res.read()
print(res)