# coding=utf-8
'''
etree 和xpath配合使用
'''
from lxml import etree

xml = etree.parse('book.xml')
s = etree.tostring(xml)
print(s)

rst = xml.xpath('//book')
print(type(rst))
print(rst)

rst = xml.xpath('//book[@category="WEB"]/year')
rst = rst[0]
print(rst)
print(rst.tag)
print(rst.text)