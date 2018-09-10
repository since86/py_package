import socket

def tcp_srv():
    # socket.AF_INET：表示ipv4协议族
    # socket.SOCK_STREAM:   表示通过TCP进行通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    addr = ('127.0.0.1',8888)

    sock.bind(addr)

    sock.listen()

    while True:
        skt, addr = sock.accept()
        msg = skt.recv(500).decode()

        rst = 'Received message:{0} from {1}'.format(msg, addr)
        print(rst)

        skt.send(rst.encode())

        skt.close()

if __name__ == '__main__':
    tcp_srv()
