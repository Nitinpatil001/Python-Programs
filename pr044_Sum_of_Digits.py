#print the sum of digits of given no.
#148 - 1+4+8 - 13
n=int(input("enter no."))
c=0
while n>=1:
    x=n%10
    c=c+x
    n=n//10
print(c)
