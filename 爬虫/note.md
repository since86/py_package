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
    
- request.date
    - 访问网络的2种方法
        - get
        - post