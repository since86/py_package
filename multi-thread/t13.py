import threading
import time
import random

class Worker(threading.Thread):
    def __init__(self, wait_num=5, index=0):
        super().__init__()
        self.wait_num = wait_num
        self.setName('窗口 '+str(index))

    def run(self):
        global counter, mutex
        while counter and self.wait_num:
            time.sleep(random.randrange(2,5))
            print(time.ctime())

            mutex.acquire()

            if counter==0:
                print(self.getName(),': 抱歉，票已售罄！')
                mutex.release()
                break

            #print('当前余票：',counter)
            counter -= 1
            print(self.getName(),'售出一张，当前余票：',counter,'张')

            mutex.release()

            self.wait_num -= 1
            self.wait_num += random.randrange(0,2)


if __name__ == '__main__':
    counter = 5
    mutex = threading.Lock()

    workers = []
    for i in range(4):
        wait_num = random.randrange(2,10)
        workers.append(Worker(wait_num, i+1))

    for w in workers:
        w.start()
