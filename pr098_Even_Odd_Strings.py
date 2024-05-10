#tuples and list- odd length strings in first list and even strings in another list
a=("ram","sham","seeta","geeta","anil","sunil","ramesh","suresh")
x=[]
y=[]
for i in a:
    c=len(i)
    if c%2==0:
        x.append(i)
    else:
        y.append(i)
print(a)
print(x)
print(y)
