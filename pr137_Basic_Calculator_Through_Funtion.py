#returning value thru function, menu driven program
def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
x=int(input("enter first "))
y=int(input("enter second "))
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
ch=int(input("enter choice: "))
if ch==1:
    z=add(x,y)
    print("addition=",z)
elif ch==2:
    z=sub(x,y)
    print("substraction=",z)
elif ch==3:
    z=mul(x,y)
    print("multiplication",z)
elif ch==4:
    z=div(x,y)
    print("division=",z)
else:
    print("wrong choice")
