"""input any string and count the no. of alphabets, digits, spaces and
special chars"""
st=input("enter string ")
a=d=s=p=0
for i in st:
    if i.isalpha():
        a=a+1
    else:
        if i.isdigit():
            d=d+1
        else:
            if i.isspace():
                s=s+1
            else:
                p=p+1
print("alpha=",a)
print("digit=",d)
print("spaces=",s)
print("special=",p)
