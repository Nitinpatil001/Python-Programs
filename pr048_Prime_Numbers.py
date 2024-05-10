#input any no. and check whether its prime or not
#the no. which is complitely divisible by 1 and itself only
n=int(input("enter no."))
cnt=0
a=1
while a<=n:
    c=n%a
    if c==0:
        cnt=cnt+1
    a=a+1
if cnt==2:
    print("prime")
else:
    print("not prime")
