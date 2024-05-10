#list
ls=[12,4,3,32,4,43,4,54]
a=ls.copy()
print(ls)
ls.append(29)
print(ls)
ls.clear()
print(ls)
print(a)
print(a.count(4))
print(a.count(74))
b=[1,7,8,9]
print(a)
print(b)
a.extend(b)
print(a)
print(a.index(4))
#print(a.index(89))-display error if not found
a.insert(3,99)
print(a)
a.pop()#pop the last value
print(a)
a.pop(3)#pop the value of given location(removes)
print(a)
a.remove(7)#removes the value
print(a)
a.reverse()
print(a)
a.sort()
print(a)

