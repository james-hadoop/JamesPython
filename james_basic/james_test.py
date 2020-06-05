import base64

str2 = '[B@63f16350'
byte = base64.decodebytes(str2.encode())
print(byte)
