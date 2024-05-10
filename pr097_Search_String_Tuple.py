#tuples - search the given string in tuple
a=("ram","sham","seeta","geeta","anil","sunil","ramesh","suresh")
st=input("enter string")
x=a.count(st)
if x>0:
    c=a.index(st)
    print("its available at ",c,"location")
else:
    print("not available")

