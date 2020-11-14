import requests

headers = {
    'Content-Type': 'application/json; charset=UTF-8',
}

data = '{"area": "全国"}'

response = requests.post('http://www.yuanqucha.com/index.php/User/Industry/SelectIndustry', headers=headers,
                         data=data.encode("utf-8"))

print(response.text.encode("utf-8"))
