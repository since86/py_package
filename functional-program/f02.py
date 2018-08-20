def funA(n):
    return n*100

def funB(n):
    return  funA(n)*3

print(funB(9))

# 高阶函数
def funC(n,f):
    return f(n)*3

print(funC(9,funA))