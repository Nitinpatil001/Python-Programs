#input any string and check whether its palindrom or not
#radar its reverse radar
st=input("enter string ")
r=""
for i in range(len(st)-1,-1,-1):
    r=r+st[i]
if r==st:
    print("palindrom")
else:
    print("not palindrom")
