def simple_coroutine(a):
    print('-> start')

    b = yield a
    print('-> receive', a ,b)

    c = yield a+b
    print('-> receive', a, b, c)


if __name__ == '__main__':
    sc = simple_coroutine(5)
    aa = next(sc)
    print(aa)

    bb = sc.send(6)
    print(bb)
    print(int(False),int(True))

    cc = sc.send(7)
    print(cc)
    print('Done')