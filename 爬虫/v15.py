# coding=utf-8
from urllib import request, error, parse
from http import cookiejar

# 创建FileCookieJar实例
cookie = cookiejar.MozillaCookieJar()
# 读取cookie
cookie.load('cookie.txt',ignore_discard=True, ignore_expires=True)
# 生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 生成https请求管理器
https_handler = request.HTTPSHandler()

#请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def getHomePage():
    url = 'https://home.cnblogs.com/u/wallfacer/'

    rsp = opener.open(url)
    html = rsp.read().decode()
    with open('rsp.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    print(cookie)
    getHomePage()