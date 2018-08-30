import multiprocessing
from time import ctime,sleep


class ClockProcess(multiprocessing.Process):
    def __init__(self,interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            print('this time is:',ctime())
            sleep(self.interval)

if __name__ == '__main__':
    p = ClockProcess(5)
    p.start()