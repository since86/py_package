def odd():
    print('step 1')
    #yield负责返回
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3

def fib(max):
    n, a, b = 0, 0, 1
    while n<max:
        print(b)
        a, b = b, a+b
        n += 1
    print('Done')

def gfib(max):
    n, a, b = 0, 0, 1
    while n<max:
        yield b
        a, b = b, a+b
        n += 1
    print('Done')

if __name__ == '__main__':
    g = odd()
    one = next(g)
    print(one)
    two = next(g)
    print(two)

    fib(5)

    g = gfib(5)
    for i in range(6):
        rst = next(g)
        print(rst)