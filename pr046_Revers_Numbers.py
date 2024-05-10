#input any no. and print the no. in reverse
n=int(input("enter no."))
c=0
while n>=1:
    x=n%10
    c=c*10+x
    n=n//10
print(c)
