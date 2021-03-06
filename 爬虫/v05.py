'''
request.Request
parse模拟post请求
F12打开，利用Network-All-Headers查看
'''
from urllib import request, parse
import json

baseUrl = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'girl'
}

# parse模块对data编码
data = parse.urlencode(data).encode()

#构造一个请求头
#包括Content-Length

headers = {
    'Content-Length': len(data)
}

#构造一个Request实例
#req = request.Request(baseUrl, data, headers)
req = request.Request(url=baseUrl, data=data, headers=headers)

rsp = request.urlopen(req)

json_data = rsp.read().decode('utf-8')
print(type(json_data), json_data)

json_data = json.loads(json_data)
print(type(json_data),json_data)

for item in json_data['data']:
    print(item['k'],'--',item['v'])