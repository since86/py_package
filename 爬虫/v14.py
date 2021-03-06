# coding=utf-8
from urllib import request, error, parse
from http import cookiejar

filename = 'cookie.txt'
# 创建FileCookieJar实例
cookie = cookiejar.MozillaCookieJar(filename)
# 生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 生成https请求管理器
https_handler = request.HTTPSHandler()

#请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    # form action提取
    url = 'https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fhome.cnblogs.com%2F'

    #登录form内容
    data = {
        'input1' : 'bravoo',
        'input2' : 'w19890816'
    }

    data = parse.urlencode(data)

    req = request.Request(url=url, data=data.encode())
    # 使用opener发起请求
    rsp = opener.open(req)

    # 保存cookie到文件
    cookie.save(ignore_discard=True,ignore_expires=True)


if __name__ == '__main__':
    login()