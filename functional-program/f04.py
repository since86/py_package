from functools import reduce

def myAdd(x,y):
    return x + y

rs = reduce(myAdd,['a','b','c','56','d'])
print(type(rs))
print(rs)