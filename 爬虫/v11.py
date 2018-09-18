from urllib import request, error

# coding:utf-8
if __name__ == '__main__':
    url = 'https://www.imooc.com/u/6539596'

    headers = {
        'Cookie': 'imooc_uuid=974c61fb-2eb3-47ec-9783-0f7232741765; imooc_isnew_ct=1522228217; PHPSESSID=qjpnbnes0224u8b70hto1i9q55; imooc_isnew=2; cninfo=bdqdkj-5931f8e07e353edf2b94a098f44a062c; UM_distinctid=1628fd1f6dd234-037ab6b41b7ad3-4542072c-1fa400-1628fd1f6de236; CNZZDATA1261110065=329702171-1522827553-https%253A%252F%252Fwww.baidu.com%252F%7C1522827553; IMCDNS=0; Hm_lvt_fb538fdd5bd62072b6a984ddbc658a16=1537190018; Hm_lvt_f0cfcccd7b1393990c78efdeebff3968=1537190018; loginstate=1; apsid=M1ZGMxMWZjZWI1OGU1ZjVkZDdjNTlmZWQxMTVjNDUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANjUzOTU5NgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGIzMWVlOTlkODVlMWQxNDUzZjEzZjFjMDQ3ZjExODgyDaifWw2on1s%3DYm; Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968=1537190062; Hm_lpvt_fb538fdd5bd62072b6a984ddbc658a16=1537190063; cvde=5af92ae0622ca-412'
    }

    req = request.Request(url=url, headers=headers)
    rsp = request.urlopen(req)

    print(rsp.headers)
    print(dir(rsp))
    html = rsp.read().decode()

    with open('rsp.html', 'w', encoding='utf-8') as f:
        f.write(html)
