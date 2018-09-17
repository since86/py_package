# 爬虫
- Python网络包简介
    - *urllib,urllib3,httplib3,*requests
    
# urllib
- 模块
    - urllib.request: 打开和读取url
    - urllib.error: 包括urllib.request产生常见的错误，包括try捕捉
    - urllib.parse: 包含解析url的方法
    - urllib.robotparse: 解决robot.txt文件
    - 案例v01
       
- 网络编码问题解决
    - chardet可以自动检测页面编码格式（不保证完全正确）
    
- urlopen的返回对象 
    - geturl
    - info: meta信息
    - getcode: 响应吗
    
- request.data 
    - 访问网络的2种方法
        - get v03
            - 利用参数给服务器传信息
            - 参数为dict，然后用parse传码
        - post v04
            - 一般向服务器传递参数
            - post把信息加密处理
            - 如果想要使用post，需要使用data参数
            - http的请求头需要修改
                - Content-Type: application/x-www.form-urlencode
                - Content-Length: 数据长度
                - 一旦更改请求方法，头部信息相适应
            - urllib.parse.urlencode可以将字符串自动转换成上面的格式
            
            - 更多的设置请求信息，需要利用request.Request v05
            
- urllib.error 
    - OSError - URLError - HTTPError
    - URLError产生的原因 v06
        - 断网
        - 服务器链接失败
        - 指向不到指定服务器
        - 是OSError子例
        
    - HTTPError v07
        - URLError的子类
        
- UserAgent v08
    - UserAgent: 用户代理，简称UA，属于headers的一部分，服务器通过UA判断访问者身份
    
    - 设置UA
        - headers
        - add_header
        
- ProxyHandler处理(代理服务器)
    - 使用代理ip，是爬虫的常用手段
    - 获取代理服务器的地址
        - www.xicidaili.com
        - www.goubanjia.com
        
    - 代理隐藏在真实访问中，代理不允许频繁访问同一个网站，所以，代理一定要很多
    
    - 使用步骤 v09
        - 设置代理地址
        - 创建ProxyHandler
        - 创建Opener
        - 安装Opener
  
- cookie & session
    - cookie存放在用户端，session服务器端
    - cookie不安全
    - session会保存在服务器上一段时间，会过期
    - 单个cookie数据不超过4k，很多浏览器限制一个站点最多存储20个
    - session一般放在内存或者数据库中
    - 没有cookie登录 v10
    
    - 使用cookie登录
        - 直接把cookie复制下来，然后手动放入请求头 v11
        
        - http模块包含一些关于cookie的模块，可以自动使用模块 
            - CookieJar
                - 存储管理cookie，向传出的http请求添加cookie
                - cookie存储在内存里，CookieJar实例回收后cookie消失
            - FileCookieJar(filename,delayload=None,policy=None)
                - 使用文件管理cookie
                - filename是保存cookie的文件
            - MozillaCookieJar(filename,delayload=None,policy=None)
                - 创建与Mozilla浏览器cookie.txt兼容的FileCookieJar实例
            - LwpCookieJar
                - 创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
                
            - CookieJar -> FileCookieJar -> MozillaCookieJar & LwpCookieJar
            
        - 利用CookieJar流程 v12
            - 打开登录网页自动通过用户名密码登录
            - 自动提取反馈回来的cookie
            - 利用提取的cookie登录隐私页面
            