l =[1,2,3,4,5,6,7]
def funA(n):
    return n*n

l1 = map(funA,l)

for i in l1:
    print(i,end=' ')