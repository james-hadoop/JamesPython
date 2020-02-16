import json
import urllib

url = 'http://localhost:8088/v1/service/user/getVerifyCode?hUserPhoneNr=15821615886'
req = urllib.Request(url)
res = urllib.urlopen(req)
res = res.read()
print(res)
