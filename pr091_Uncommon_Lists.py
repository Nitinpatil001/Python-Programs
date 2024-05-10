"""create third list which having all elements of a which are
not available in b(a-b) and vise versa"""
a=[1,3,5,7,9]
b=[1,2,4,6,9]
c=[]
d=[]
for i in a:
    x=b.count(i)
    if x==0:
        c.append(i)
for i in b:
    x=a.count(i)
    if x==0:
        d.append(i)
print(a)
print(b)
print(c)
print(d)
