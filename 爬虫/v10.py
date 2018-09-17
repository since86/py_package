from urllib import request, error
#coding:utf-8
if __name__ == '__main__':
    url = 'https://www.imooc.com/u/6539596'
    rsp = request.urlopen(url)
    html = rsp.read().decode()
    print(html)
    with open('rsp.html','w', encoding='utf-8') as f:
        f.write(html)
