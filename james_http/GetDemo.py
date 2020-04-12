import urllib
# import urllib2

url = 'http://localhost:8088/v1/service/user/getVerifyCode?hUserPhoneNr=13621936820'
req = urllib.Request(url)
res = urllib.urlopen(req)
res = res.read()
print(res)
