#errors/exception handling(user define)
class myerr(Exception):
    pass
n=int(input("enter no."))
try:
    if n<0:
        raise myerr
    else:
        print("nice no.")
except myerr:
    print("no. must be positive")
