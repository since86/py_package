#issubclass isinstance
class A():
    name = 'eric'

    def do(self):
        pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(A,B))
print(issubclass(B,A))
print(issubclass(C,object))

a = A()
print(isinstance(a,A))

print(hasattr(a,'name'))
print(hasattr(a,'do1'))
print(hasattr(A,'name'))
print('*'*20)
print(getattr(A,'name'))

print(dir(A))
print(dir(a))
print(A.__dict__)