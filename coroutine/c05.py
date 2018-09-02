from collections import namedtuple

ResClass = namedtuple('Res','count average')

def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield
        #None是哨兵值
        if term == None:
            break

        total += term
        count += 1
        average = total/count

    return ResClass(count,average)

#委派生成器
def grouper(storages, key):
    while True:
        storages[key] = yield from averager()

def client():
    process_data ={
        'boys_2' : [39.0,40.8,22.5,55.4,88.2],
        'boys_1' : [47,38.4,25.0,68,77,15]
    }

    storages = {}
    for k,v in process_data.items():
        #获得协程
        coroutine = grouper(storages,k)
        #预激协程
        next(coroutine)
        #发送数据到协程
        for dt in v:
            coroutine.send(dt)
        #终止协程
        coroutine.send(None)

    print(storages)

if __name__ == '__main__':
    client()