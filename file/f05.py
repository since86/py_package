import shelve
#shelve的写入
shv = shelve.open(r'shv.db')
shv['one'] = 1
shv['two'] = 2
shv['three'] = 3
shv.close()

#shelve的读取
shv = shelve.open(r'shv.db')
try:
    print(shv['one'])
    print(shv['two'])
    print(shv['three'])
    print(shv['four'])
except Exception as e:
    print(e)
finally:
    shv.close()

with shelve.open(r'shv.db') as shv:
    shv['one'] = {'a':1, 'b':2, 'c':3}
    print(shv['one'])

with shelve.open(r'shv.db',writeback=True) as shv:
    s = shv['one']
    s['a'] = 100
    print(shv['one'])
