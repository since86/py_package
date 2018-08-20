a = [21515,511,7874,18,15466,4546,2495,26]
al = sorted(a,reverse=False)
print(a)
print(al)

a1 = [-44,555,2,66,-7879]
al1 = sorted(a1,key=abs,reverse=True)
print(al1)

astr = ['dana','eric','brooks','Zoom','dRik']
astr1 = sorted(astr)
astr2 = sorted(astr,key=str.upper)
print(astr1,astr2)

