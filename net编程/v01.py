'''
server端编程
    - 建立socket
    - 绑定，为socket指定固定的端口和ip
    - 接受对方发出内容
    - 给对方发送反馈信息（非必须）
'''
import socket

def serverFunc():
    # socket.AF_INET:使用ipv4协议族
    # socket.SOCK_DGRAM:使用udp通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ('127.0.0.1',8080)
    sock.bind(addr)

    # ewcvfrom参数是缓冲区大小，返回的是一个tuple，前一项表示数据，后一项表示地址
    data, addr =sock.recvfrom(500)
    print(type(data))
    print(data)

    # 接收的数据是byte类型的数据，需要解码才能得到str
    # decode默认解码utf-8
    text = data.decode()
    print(type(text))
    print(text)

    # 反馈给客户端
    rsp = 'received--from server'
    data = rsp.encode()
    sock.sendto(data,addr)

if __name__ == '__main__':
    print('Starting server...')
    serverFunc()
    print('End server...')

