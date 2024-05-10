"""create third list with all elements of a and b(just like union) """
a=[1,1,3,5,7,9]
b=[1,2,2,4,6,9]
c=[]
for i in a:
    x=c.count(i)
    if x==0:
        c.append(i)
for i in b:
    x=a.count(i)
    z=c.count(i)
    if x==0 and z==0:
        c.append(i)
print(a)
print(b)
print(c)
