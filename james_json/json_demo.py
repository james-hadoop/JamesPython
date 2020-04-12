import json

f = open('../demo.json', 'r')

data = f.read()
"""
    把json转成字典
"""
json_dict = json.loads(data)

print(json_dict['name'])
f.close()

dic = {
    "name": "james",
    "age": 18
}

"""
    把字典转成json
"""
json_obj = json.dumps(dic)

f = open('json_demo2.json', 'w')
f.write(json_obj)
f.close()
