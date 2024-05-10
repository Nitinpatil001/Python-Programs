"""create third list with common elements of a and b(just like intersect) """
a=[1,3,5,7,9]
b=[1,2,4,6,9]
c=[]
for i in b:
    x=a.count(i)
    if x>0:
        c.append(i)
print(a)
print(b)
print(c)
