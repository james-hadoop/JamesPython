import base64
import re

expression = 'KChrYW5kaWFuX29kc19hbGxfY29tbWVudF9jb216YW5fZC5mdGltZSA9IDIwMjAwNjA3KSBhbmQg\r\na2FuZGlhbl9vZHNfYWxsX2NvbW1lbnRfY29temFuX2Qucm93a2V5IGlzIG5vdCBudWxsKQ=='
clean_expression = re.sub('[\s+]', '', expression)

bb = base64.decodebytes(clean_expression.encode())
print(bb.decode("utf-8"))
