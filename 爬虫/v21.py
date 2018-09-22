# coding=utf-8
'''
使用headers和parmas
研究返回结果
'''
import requests

url = 'http://www.baidu.com/s?'

kw = {
    'wd' : '王八'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

rsp = requests.get(url=url, params=kw, headers=headers)

print(rsp.text)
print(rsp.encoding)
print(rsp.status_code)
print(rsp.content)
print(rsp.url)

