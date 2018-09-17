from urllib import request, error

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    try:
        '''
        使用headers方法
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

        req = request.Request(url=url, headers=headers)
        '''

        # 使用add_header方法
        req = request.Request(url)

        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')

        rsp = request.urlopen(req)
        print(rsp.headers)

        html = rsp.read().decode()
    except error.URLError as e:
        print(e)
