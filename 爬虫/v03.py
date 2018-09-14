from urllib import request, parse

if __name__ == '__main__':
    url = 'http://www.baidu.com/s?'
    wd = input('enter your keyword:')

    qs = {
        'wd' : wd
    }

    qs = parse.urlencode(qs)
    fullurl = url+qs

    resp = request.urlopen(fullurl)
    html = resp.read()

    print(type(resp),resp.geturl(),resp.getcode())
    print(resp.info())
    html = html.decode()

    #print(html)