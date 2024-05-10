"""
input employee no, and payment of employee and calculate increment
if pay<=500 - incr is 15% of payment
if pay<=1500 - incr is 10% of payment
if pay>1500 - incr is 0
print increment """
en=int(input("enter employee no."))
ep=int(input("enter employee payment"))
if ep<=500:
    inc=ep*15/100
else:
    if ep<=1500:
        inc=ep*0.10
    else:
        inc=0
print(inc)
        
