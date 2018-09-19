# coding=utf-8
'''
破解有道词典
'''
from urllib import request, parse

def youdao(key):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    data = {
        'i': 'girl',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1537341592629',
        'sign': '33c71b25d21e947fc7422df503601b2c',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        'typoResult': 'false'
    }

    data = parse.urlencode(data).encode()

    headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Content-Length':'207',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'ANTICSRF=cleared; P_INFO=m15357774587@163.com|1528967953|2|163|00&99|null&null&null#anh&340100#10#0#0|153587&1||15357774587@163.com; OUTFOX_SEARCH_USER_ID=-313146237@10.169.0.84; JSESSIONID=aaahY9u-_OQdXcRfgSWxw; OUTFOX_SEARCH_USER_ID_NCOO=2073854141.844427; ___rl__test__cookies=1537341592621',
        'Host':'fanyi.youdao.com',
        'Origin':'http://fanyi.youdao.com',
        'Referer':'http://fanyi.youdao.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
    }

    req = request.Request(url, data=data, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()

    print(html)

if __name__ == '__main__':
    youdao('girl')