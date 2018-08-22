# 读取test01.txt内容，每3个字休息1s
import time
with open(r'test01.txt', 'r', encoding='utf-8') as f:
    strChar = f.read(3)
    while strChar:
        print(strChar)
        print('*'*10)
        #time.sleep(2)
        strChar = f.read(3)

with open(r'test01.txt', 'r', encoding='utf-8') as f:
    strChar = f.read(3)
    pos = f.tell()
    while strChar:
        print(pos)
        print(strChar)
        strChar = f.read(3)
        pos = f.tell()