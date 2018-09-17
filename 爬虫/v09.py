from urllib import request, error

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    proxy = {'http':'47.105.132.206:80','http':'118.190.208.228:80'}

    proxy_handler = request.ProxyHandler(proxy)

    opener = request.build_opener(proxy_handler)

    request.install_opener(opener)

    try:
        rsp = request.urlopen(url)
        print(rsp.info())
        html = rsp.read().decode()
        #print(html)

    except error.URLError as e:
        print(e)

    except Exception as e:
        print(e)