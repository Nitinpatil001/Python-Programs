"""input emailid and check whether its valid or not"""
st=input("enter emailid")
c=s=a=d=p=sm=dg=0
for i in st:
    if i.isupper():
        c=c+1
    elif i.isspace():
        s=s+1
    elif i=="@":
        a=a+1
    elif i==".":
        d=d+1
    elif i.isdigit():
        dg=dg+1
    elif i.islower():
        sm=sm+1
    else:
        p=p+1
if c>0 or s>0 or p>0 or d==0 or a!=1:
    print("invalid emailid")
else:
    print("valid emailid")
    
