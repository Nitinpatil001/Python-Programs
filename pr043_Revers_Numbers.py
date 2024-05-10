#input any no. and print its digits in reverse
#184 - 4 8 1
n=int(input("enter no."))
while n>=1:
    x=n%10
    print(x)
    n=n//10
