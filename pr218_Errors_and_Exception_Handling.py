#errors/exception handling
x=[12,32,43,55]
try:
    a=int(input("enter first no."))
    b=int(input("enter second no."))
    c=a/b
    print(c)
    print(x[9])
except ZeroDivisionError:
    print("dont divide the no. by zero")
except ValueError:
    print("input numeric values only")
except IndexError:
    print("check the array size")
