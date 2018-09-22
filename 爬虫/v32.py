# coding=utf-8
import requests
from lxml import etree
from bs4 import BeautifulSoup

url = 'http://www.welvx.com'

rsp = requests.get(url)
page = etree.HTML(rsp.text)

tag_a = page.xpath('/html/head/link[@type="image/x-icon"]')
for item in tag_a:
    print(item.values())

s = page.xpath('//label')
for item in s:
    print(item.text)