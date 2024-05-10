#set
a={1,3,5,7,9}
b={1,2,4,6,9}
print(a)
print(b)
print(a.difference(b))
print(b.difference(a))
a.discard(3)
print(a)
a.discard(11)# no action will be taken if its not available, even no error msg
print(a)

