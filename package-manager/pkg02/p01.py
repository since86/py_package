# 包含一个学生类
# 一个sayHello函数
# 一个打印语句

class  Student():
    def __init__(self,name='NoName',age=18):
        self._name = name

    def say(self):
        print('你好，我是{0}'.format(self._name))

def sayHello():
    print('模块实例')

#此语句建议一直作为程序入口
if __name__ =='__main__':
    print('当前是p01模块！')