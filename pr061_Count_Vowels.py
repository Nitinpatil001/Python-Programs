#input any string and count its vowels
st=input("enter string ")
cnt=0
for i in st:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        cnt=cnt+1
print("vowels are ",cnt)    
