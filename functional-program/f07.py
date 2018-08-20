def myF1():
    def myF2():
        print('in myF2')
        return 2
    return myF2

f = myF1()
f()

print(f())

def myF3( *args):
    def myF4():
        rst = 0
        for i in args:
            rst += i
        return rst
    return myF4

f1= myF3(1,2,3,4,5,6)
print(f1())

def count():
    rst=[]
    for i in range(1,4):
        def f():
            return i*i
        rst.append(f)
    return rst

c1,c2,c3 = count()
print(c1(),c2(),c3())

def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

c01,c02,c03 = count1()
print(c01(),c02(),c03())
