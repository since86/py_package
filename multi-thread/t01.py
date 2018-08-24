'''
利用time函数生成2个函数
顺序调用
计算总的运算时间
'''
import time
def loop1():
    print('start loop1 at: ',time.ctime())
    time.sleep(3)
    print('end loop1 at: ',time.ctime())

def loop2():
    print('start loop21 at: ',time.ctime())
    time.sleep(2)
    print('end loop2 at: ',time.ctime())

def main():
    print('starting at:',time.ctime())
    loop1()
    loop2()
    print('ending at:',time.ctime())

if __name__ == '__main__':
    main()
