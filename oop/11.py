# 元类
class WelvxMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['id'] = '000000'
        attrs['choose'] = '自由行'
        return type.__new__(cls, name, bases, attrs)

class Intercity(object,metaclass=WelvxMetaClass):
    pass

i = Intercity()
print(i.id)
print(i.choose)


