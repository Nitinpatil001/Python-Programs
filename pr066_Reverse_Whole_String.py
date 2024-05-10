#print the whole string in reverse
st=input("enter string ")
r=""
for i in range(len(st)-1,-1,-1):
    r=r+st[i]
print(r)
