#input any no. and check whether its palindrom or not
#121 -its reverse is again - 121
n=int(input("enter no."))
p=n
c=0
while n>=1:
    x=n%10
    c=c*10+x
    n=n//10
if p==c:
    print("palindrom")
else:
    print("not palindrom")
