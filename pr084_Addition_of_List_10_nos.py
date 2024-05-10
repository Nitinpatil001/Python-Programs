"""input 10 nos using list and print addition of all elements"""
ls=[]
for i in range(10):
    n=int(input("enter no."))
    ls.append(n)
c=0
for i in range(10):
    c=c+ls[i]
print("addition=",c)
    
