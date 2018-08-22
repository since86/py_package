with open(r'test01.txt','r', encoding='utf-8') as f:
    #按行读取内容
    strline = f.readline()
    while strline:
        print(strline)
        strline = f.readline()

with open(r'test01.txt','r', encoding='utf-8') as f:
    l = list(f)
    for line in l:
        print(line)

with open(r'test01.txt', 'r', encoding='utf-8') as f:
    strChar = f.read(3)
    print(len(strChar))
    print(strChar)

print('*'*30)
with open(r'test01.txt', 'r', encoding='utf-8') as f:
    # 一个汉字字节是3
    f.seek(6, 0)

    strChar = f.read()
    print(strChar)

