import threading
from time import sleep,ctime

loop = [4,2]

class ThreadFunc():
    def __init__(self, name):
        self.name = name

    def loop(self, nloop, nsec):
        print('Start loop',nloop, 'at', ctime())
        sleep(nsec)
        print('End loop',nloop, 'at', ctime())

def main():
    print('Starting at', ctime())
    t = ThreadFunc('loop')
    # t1 和t2的定义方式相等
    t1 = threading.Thread(target=t.loop, args=('Loop1',4))
    t2 = threading.Thread(target=ThreadFunc('loop').loop, args=('Loop2', 2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('All Done!!!')

if __name__ == '__main__':
    main()
