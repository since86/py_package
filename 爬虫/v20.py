# coding=utf-8
import requests

url = 'http://www.baidu.com'

rsp = requests.get(url)
print(type(rsp),rsp)

print(rsp.text)
print(type(rsp.text))

rsp = requests.request('get',url)
print(len(rsp.text))