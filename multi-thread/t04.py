import threading
import time
def loop1(in1):
    print('start loop1 at:',time.ctime())
    print('我是参数：',in1)
    time.sleep(2)
    print('end loop1 at:',time.ctime())

def loop2(in1,in2):
    print('start loop2 at:',time.ctime())
    print('我是参数',in1,'和参数',in2)
    time.sleep(3)
    print('end loop2 at:',time.ctime())

def main():
    print('Starting at:',time.ctime())
    t1 = threading.Thread(target=loop1,args=('老王',))
    t2 = threading.Thread(target=loop2, args=('小李','老李'))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('All done at:', time.ctime())

if __name__ =='__main__':
    main()