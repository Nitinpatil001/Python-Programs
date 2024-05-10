"""print the addition of two list """
a=[]
b=[]
c=[]
for i in range(10):
    n=int(input("enter a element"))
    a.append(n)
for i in range(10):
    n=int(input("enter b element"))
    b.append(n)
for i in range(10):
    d=a[i]+b[i]
    c.append(d)
for i in range(10):
    print(a[i],"+",b[i],"=",c[i])
