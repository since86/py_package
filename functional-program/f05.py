def funC(n):
    return n%3 == 0

l = [0,1,2,3,4,5,6,7,8,9]

fs = filter(funC,l)
print(type(fs))
for i in fs:
    print(i)