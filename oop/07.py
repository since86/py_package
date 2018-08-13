class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def fget(self):
        return self._name*2

    def fset(self,name):
        self._name=name.upper()

    def fdel(self,name):
        self.name='Noname'

    name = property(fget,fset,fdel,'')

s = Student('eric',18)

print(s.name)