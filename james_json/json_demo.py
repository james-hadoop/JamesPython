import json

f = open('../demo.json', 'r')

data = f.read()
json_data = json.loads(data)

print(json_data['name'])
f.close()

dic = {
    "name": "james",
    "age": 18
}

data = json.dumps(dic)

f = open('json_demo2.json', 'w')
f.write(data)
f.close()
