#errors/exception handling
x=[12,32,43,55]
print(x)
try:
    n=int(input("enter no.  to search"))
    print(x.index(n))
except ValueError:
    print("value not found")
