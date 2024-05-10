"""create third list with uncommon elements of a and b """
a=[1,3,5,7,9]
b=[1,2,4,6,9]
c=[]
for i in a:
    x=b.count(i)
    if x==0:
        c.append(i)
for i in b:
    x=a.count(i)
    if x==0:
        c.append(i)
print(a)
print(b)
print(c)
