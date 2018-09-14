from urllib import request
import chardet

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    resp = request.urlopen(url)
    html = resp.read()

    print(type(resp),resp.geturl(),resp.getcode())
    print(resp.info())
    html = html.decode()

    #print(html)