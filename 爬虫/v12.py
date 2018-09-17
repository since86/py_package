# coding=utf-8
from urllib import request, error, parse
from http import cookiejar

cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)

http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

#请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    url = ''

    #登录form内容
    data = {
        'email' : '15357774587',
        'password' : 'w19890816'
    }

    data = parse.urlencode(data)

    req = request.Request(url=url, data=data.encode())
    # 使用opener发起请求
    rsp = opener.open(req)

def getHomePage():
    url = 'https://www.imooc.com/u/6539596'

    rsp = opener.open(url)
    html = rsp.read().decode()
    with open('rsp.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()






