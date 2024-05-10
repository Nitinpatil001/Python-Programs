#set
a={1,3,5,7,9}
x={1,3}
b={1,2,4,6,9}
print(a)
print(b)
print(a.intersection(b))
print(a.issubset(x))
print(x.issubset(a))
print(a.issuperset(x))
a.pop()#eliminates 1st element
print(a)
a.remove(3)
print(a)
#a.remove(44)-throws error message if not a member
