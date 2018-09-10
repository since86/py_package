'''
client端流程
    - 建立socket
    - 发送内容到服务器
    - 接收服务器返回的消息
'''
import socket

def clientFunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    text = '我是谁？'

    data = text.encode()

    sock.sendto(data, ('127.0.0.1',8080))

    data, addr= sock.recvfrom(200)

    res = data.decode()

    print(res)

if __name__ == '__main__':
    print('Starting client...')
    clientFunc()
    print('End client...')

