import calendar
import time

cal = calendar.calendar(2018,l=1,c=15)
#print(isinstance(cal,str))
print(cal)
print(calendar.isleap(2018))
print(calendar.month(2018,3))
calendar.prmonth(2018,3)
print(calendar.weekday(2018,8,17))

print('#'*40)
print(time.time())
t = time.localtime()
print(type(t))
ft = time.strftime('%Y年%m月%d日 %H时%M分',t)
print(ft)

print('*'*20)
t2 = time.asctime()
print(type(t2))
print(time.mktime(t))