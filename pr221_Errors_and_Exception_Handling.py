#errors/exception handling(user define)
class myerr(Exception):
    pass
class yourerr(Exception):
    pass
n=int(input("enter no."))
try:
    if n<0:
        raise myerr
    elif n>999:
        raise yourerr
    else:
        print("nice no.")
except myerr:
    print("no. must be positive")
except yourerr:
    print("no must be lessthan 1000")
