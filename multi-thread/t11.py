
import threading
from time import ctime

sum = 0
loopSum = 1000000
lock =threading.Lock()

def myAdd():
    global sum,loopSum
    for i in range(0,loopSum):
        #申请锁
        lock.acquire()
        sum += 1
        lock.release()

def myMinu():
    global sum,loopSum
    for i in range(0,loopSum):
        lock.acquire()
        sum -= 1
        lock.release()

if __name__ == '__main__':
    print('Starting at {0},sum = {1}'.format(ctime(),sum))
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Done at {0},sum = {1}'.format(ctime(),sum))