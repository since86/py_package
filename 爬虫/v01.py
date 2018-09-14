'''
使用urllib.request请求一个网页，并把网页打印出来
'''

from urllib import request
import chardet

if __name__ == '__main__':
    import chardet
    from urllib import request

    url = 'http://www.baidu.com'
    resp = request.urlopen(url)

    html = resp.read()
    cs = chardet.detect(html)
    print(cs)

    print(cs.get('encoding'))

    html = html.decode(cs.get('decoding','utf-8'))
    #print(html)