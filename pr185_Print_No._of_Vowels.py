#read myinfo.dat, and count the vowels of it
fp=open("myinfo.dat","r")
cnt=0
for i in fp:
    for j in i:
        if j=='a' or  j=='e' or  j=='i' or  j=='o' or  j=='u' or  j=='A' or  j=='E' or  j=='I' or  j=='O' or j=='U':
            cnt=cnt+1
fp.close()
print("vowels are ",cnt)
