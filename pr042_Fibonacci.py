#fibonacci series up to given no.
n=int(input("enter no."))
a=0
b=1
print(a)
print(b)
c=0
while c<=n:
    c=a+b
    print(c)
    a=b
    b=c
