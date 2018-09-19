# coding=utf-8
'''
n = e("./jquery-1.7");
salt = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
sign = n.md5("fanyideskweb" + e + t + "6x(ZHw]mwzX#u0V7@yfwK")
md5一共需要4个参数，第一个和第四个固定，t为salt值，e为传入的event
'''

def getSalt():
    '''
    salt公式 ："" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
    '''
    import time, random
    salt = int(time.time()*1000)+random.randint(0,10)
    return salt

def getMd5(v):
    import hashlib
    md5 = hashlib.md5()
    # update需要bytes格式
    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()
    return sign

def getSign(key,salt):
    sign = "fanyideskweb" + key + str(salt) + "6x(ZHw]mwzX#u0V7@yfwK"
    sign = getMd5(sign)
    return sign


from urllib import request, parse

def youdao(key):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    salt = getSalt()
    data = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': str(salt),
        'sign': getSign(key, salt),
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        'typoResult': 'false'
    }

    print(data)

    data = parse.urlencode(data).encode()

    headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        #'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Content-Length':str(len(data)),
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'ANTICSRF=cleared; P_INFO=m15357774587@163.com|1528967953|2|163|00&99|null&null&null#anh&340100#10#0#0|153587&1||15357774587@163.com; OUTFOX_SEARCH_USER_ID=-313146237@10.169.0.84; JSESSIONID=aaahY9u-_OQdXcRfgSWxw; OUTFOX_SEARCH_USER_ID_NCOO=2073854141.844427; ___rl__test__cookies=1537341592621',
        'Host':'fanyi.youdao.com',
        'Origin':'http://fanyi.youdao.com',
        'Referer':'http://fanyi.youdao.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
    }

    req = request.Request(url=url, data=data, headers=headers)
    rsp = request.urlopen(req)
    print(rsp)
    html = rsp.read()
    print(html.decode())

if __name__ == '__main__':
    youdao('boy')