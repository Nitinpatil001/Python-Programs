#function with default value
def add(a=10,b=20):
    c=a+b
    print(c)
x=int(input("enter first no."))#5
y=int(input("enter second no."))#7
add()#30
add(x,y)#12
add(x)#25
add(y)#27
