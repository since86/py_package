import time
import _thread as thread

def loop1():
    print('start loop1 at: ',time.ctime())
    time.sleep(3)
    print('end loop1 at: ',time.ctime())

def loop2():
    print('start loop21 at: ',time.ctime())
    time.sleep(2)
    print('end loop2 at: ',time.ctime())

def main():
    print('starting at:',time.ctime())
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())
    print('ending at:',time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)