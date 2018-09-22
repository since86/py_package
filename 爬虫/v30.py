# coding=utf-8
from urllib import request
from bs4 import BeautifulSoup
import re

url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')
content = soup.prettify()

# print(content)

for node in soup.head.contents:
    if node.name == 'meta':
        print(node)
print('=='*10)
ss = soup.find_all(re.compile('^me'))
print(ss)