# coding=utf-8
import requests
import json
from urllib import parse

baseUrl = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'girl'
}

#构造一个请求头
#包括Content-Length
headers = {
    'Content-Length': str(len(data))
}

#构造一个Request实例
#req = request.Request(baseUrl, data, headers)
rsp = requests.post(url=baseUrl, data=data, headers=headers)

print(type(rsp.text))
print(type(rsp.json()),rsp.json())

data = json.loads(rsp.text)

print(type(data))
for item in data['data']:
    print(item)