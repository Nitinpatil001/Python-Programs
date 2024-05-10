#input three nos and find out the largest of them
a=int(input("enter first "))
b=int(input("enter second "))
c=int(input("enter third "))
if a>b and a>c:
    print(a)
else:
    if b>a and b>c:
        print(b)
    else:
        print(c)
