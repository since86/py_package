import time
import threading

class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg

    #需要重写
    def run(self):
        time.sleep(2)
        print('The args for this class is {0}'.format(self.arg))

for i in range(5):
    t = MyThread(i)
    t.start()
    t.join()

print('All Done!!')