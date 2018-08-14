class Person():
    def __init__(self,age):
        self._age=age

    def fget(self):
        return int(self._age)

    def fset(self,age):
        self._age = age

    def fdel(self,age):
        pass

    age=property(fget,fset,fdel,'')

p = Person(22.5)

print(p.age)
print(Person.__name__)
print(Person.__bases__)
print(isinstance(Person.__bases__,tuple))