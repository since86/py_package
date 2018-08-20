def sayHello(name):
    print('hello,{0}'.format(name))
    print('Done...')

def getName():
    print('*' * 30)
    name = input('请输入您的姓名：')
    print(sayHello(name=name))
    print('*' * 30)


getName()