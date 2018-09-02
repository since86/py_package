def simple_coroutine():
    print('-> start')
    x = yield
    print('-> receive',x)

if __name__ == '__main__':
    sc =simple_coroutine()
    print(111)
    next(sc)

    print(222)
    sc.send('xiecheng')