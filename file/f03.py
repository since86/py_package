with open(r'test01.txt','a',encoding='utf-8') as f:
    a = '\n纸短情长啊 \n道不尽当时年少'
    f.write(a)

with open(r'test01.txt','a',encoding='utf-8') as f:
    l = ['我的故事都是','关于你呀']
    f.writelines(l)
