class A():
    def __init__(self):
        print('A的构造函数')

class B(A):
    def __init__(self,name):
        print('B的构造函数',name)

class C(B):
    def __init__(self,name):
        #B.__init__(self,name)
        super(C,self).__init__(name)
        print('C')

c = C('eric')