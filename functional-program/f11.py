import collections
#from collections import deque

Circle = collections.namedtuple('Circle',['x','y','r'])

c = Circle(100,100,50)
print(c,type(c))
print(isinstance(c,tuple))

#dequeue 双重队列
from collections import deque
q = deque(['a','b','e'])
print(type(q),q)

q.append('d')
q.appendleft('0')
x = q.index('a')
print(q,x)

from collections import defaultdict
func = lambda : 100

d = defaultdict(func)
d['one'] = 1
d['two'] = 2

print(d,d['five'],d['six'])

from collections import Counter
str1 = 'dadsdsawwq'
yy = 1234567890151414
c = Counter(str1)
d = str(yy)
print(c)
print(Counter(d))
