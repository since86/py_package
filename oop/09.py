#魔术方法

'''
__init__ 构造函数
__new__ 对象实例化
__call__
'''

class A():
    def __init__(self,name):
        self._name = name
        print('函数初始化')

    def __call__(self):
        print('函数被调用')

    def __gt__(self, other):
        print('{0}比{1}大吗？'.format(self._name,other._name))
        return self._name > other._name

    def __setattr__(self, key, value):
        print('设置{0}'.format(key))
        super().__setattr__(key,value)

    @staticmethod
    def do():
        pass

a = A('br')
a.age=18
a.do()
print(a)
print(a.age)

a1 = A('eric')
a2 = A('andy')

print(a1 > a2)
#a()