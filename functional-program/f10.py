l = [0,1,2,3,4,5]
l1 = [11,22,33,44,55,66]

z = zip(l,l1)
print(type(z),z)
for i in z:
    print(i)

l = [11,22,33,44,5656]
em = enumerate(l,start=10)

print(type(em),em)

l1 = [i for i in em]
print(l1)