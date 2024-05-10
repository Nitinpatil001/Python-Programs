#functions continue
#menu driven program
def add():
    a=int(input("enter first "))
    b=int(input("enter second "))
    c=a+b
    print(c)
def sub():
    a=int(input("enter first "))
    b=int(input("enter second "))
    c=a-b
    print(c)
def mul():
    a=int(input("enter first "))
    b=int(input("enter second "))
    c=a*b
    print(c)
def div():
    a=int(input("enter first "))
    b=int(input("enter second "))
    c=a/b
    print(c)

print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
ch=int(input("enter choice"))
if ch==1:
    add()
elif ch==2:
    sub()
elif ch==3:
    mul()
elif ch==4:
    div()
else:
    print("wrong choice")
