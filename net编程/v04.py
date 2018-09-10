import socket

def tcp_cli():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('127.0.0.1',8888)

    sock.connect(addr)

    msg = '我是TCP客户端'
    msg = msg.encode()

    sock.send(msg)

    rsp = sock.recv(500)
    print(rsp.decode())

    sock.close()

if __name__ == '__main__':
    tcp_cli()