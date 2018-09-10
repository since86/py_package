import multiprocessing
from time import ctime
from collections import Iterable,Iterator
def consumer(input_q):
    print('Into consumer:',ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print('pull', item, 'out of q')
        input_q.task_done()

    print('Out of consumer:', ctime())

def producer(sequeue, output_q):
    print('Into producer:', ctime())
    for item in sequeue:
        output_q.put(item)
        print('put', item, 'into q')
    print('Out of producer:', ctime())

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()

    l = [1,2,3,4]
    print(isinstance(l,Iterable))
    print(isinstance(l,Iterator))

    ll = iter(l)
    print(isinstance(ll,Iterator))
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    #cons_p.daemon = True
    cons_p.start()

    sequeue = [1,2,3,4]
    producer(sequeue, q)

    #哨兵,多少进程对应多少哨兵
    q.put(None)
    cons_p.join()
