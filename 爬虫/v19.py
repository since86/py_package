# coding=utf-8
'''
ajax的url
https://movie.douban.com/j/chart/top_list?type=11&interval_id=80%3A70&action=&start=120&limit=20
'''
from urllib import request
import json

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=80%3A70&action=&start=0&limit=200'

rsp = request.urlopen(url)
data = rsp.read().decode()
print(type(data))

with open('douban.txt','w',encoding='utf-8') as f:
    f.write(data)

data  = json.loads(data)



print(type(data))
print(data)

