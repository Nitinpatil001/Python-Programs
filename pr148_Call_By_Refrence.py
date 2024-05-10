#iterations are by default call by reference
def show(x):
    print("after passing")
    print(x)
    x.append(199)

a=[12,32,43,54,99]
print("before passing ")
print(a)
show(a)
print("after returning")
print(a)
