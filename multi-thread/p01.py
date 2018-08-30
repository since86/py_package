import multiprocessing
from time import sleep,ctime

def clock(interval):
    while True:
        print('this time is:',ctime())
        sleep(interval)

if __name__ == '__main__':
    p = multiprocessing.Process(target=clock,args=(3,))
    p.start()