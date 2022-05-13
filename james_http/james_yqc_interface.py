import json
import urllib

url = 'www.baidu.com'
req = urllib.Request(url)
res = urllib.urlopen(req)
res = res.read()
print(res)
