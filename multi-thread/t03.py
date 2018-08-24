import time
import _thread as thread

def loop1(in1):
    print('start loop1 at:',time.ctime())
    print('我是参数：',in1)
    time.sleep(2)
    print('end loop1 at:',time.ctime())

def loop2(in1,in2):
    print('start loop2 at:',time.ctime())
    print('我是参数：',in1,'和参数',in2)
    time.sleep(3)
    print('end loop2 at:',time.ctime())

def main():
    print('Starting at:',time.ctime())
    thread.start_new_thread(loop1,('老王',))
    thread.start_new_thread(loop2,('老李','小李'))
    print('All done at:', time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)