# UDP编程案例： v01，v02
# TCP编程：v03,v04
   - 面对链接的传输，每次传输之前需要先建立一个链接
   - 客户端和服务器端两个程序需要编写
        - server端：
             1. 建立socket负责具体通信，这个socket只负责接受对方的请求
             2. 绑定端口和地址
             3. 监听接入的访问socket
             4. 接受访问的socket，即建立了一个通信的链接通路
             5. 利用接收到的socket接受对方的访问内容
             6. 如果有必要，向对方发送反馈信息
             7. 关闭链接通路
             
        - client端：
             1. 建立通信socket
             2. 链接对方，请求与对方通信
             3. 发送内容到服务器
             4. 接受对方的反馈
             5. 关闭链接通路

# FTP编程（FileTransferProtocal) v05

# Python for mail
- SMTP协议负责发送邮件 
    - 使用email模块构造邮件
        - 纯文本 v07
        - HTML v08
        - 带附件 v09
            - 可以看做一个文本邮件和一个附件的合体(MIMEMultipart)
            
        - 添加邮件头，抄送等信息 v10
            - mail['FROM']
            - mail['TO']
            - mail['Subject']
            
        - 同时支持html和text格式 v11
            - 构建一个MIMEMultipart格式邮件
            - MIMEMultipart设置成alternative
            - 添加html和text附件
        - 使用smtplib模块发送邮件
- POP3协议负责接收邮件 v12
    - 本质上是从MDA到MUA的过程
    - 从MDA下载下来的是一个完整的邮件结构体，需要解析
    - 步骤：
        1. 用poplib下载邮件结构体原始内容
            1. 准备相应的内容（邮件地址，密码，POP3实例）
            2. 身份认证
            3. 一般会得到邮箱内邮件的整体列表
            4. 根据相应序号，得到某一份邮件的数据流
            5. 利用解析函数进行解析出邮件结构体
        2. 用email解析邮件的具体内容
            