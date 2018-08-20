import functools
#输入16进制的数字，得到十进制
def c16(n,base=16):
    return int(n,base)

print(c16('12345'))

int16 = functools.partial(int, base=8)
print(int16('12345'))