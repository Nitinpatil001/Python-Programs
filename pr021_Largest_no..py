#input three nos and find out the largest of them
a=int(input("enter first "))
b=int(input("enter second "))
c=int(input("enter third "))
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)
