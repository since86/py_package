from urllib import request, error

if __name__ == '__main__':
    url = 'http://www.baiiiiiiiiidu.com'

    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.URLError as e:
        print('URLError: {0}'.format(e.reason))

    except Exception as e:
        print('exception: {0}'.format(e))
