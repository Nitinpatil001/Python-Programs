#read myinfo.dat, and count alphabets,digits,spaces, and special chrs 
fp=open("myinfo.dat","r")
a=d=s=p=0
for i in fp:
    for j in i:
        if j.isalpha():
            a=a+1
        elif j.isdigit():
            d=d+1
        elif j.isspace():
            s=s+1
        else:
            p=p+1
print("alphabets are ",a)
print("digits are ",d)
print("spaces are ",s)
print("special are ",p)
