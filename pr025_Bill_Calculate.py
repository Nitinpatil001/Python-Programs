"""
input units and calculate the bill as
for first 100 units rate is 40ps/unit
for next 200 units rate is 50ps/unit
beyond 300 units rate is 60ps/unit
print the bill
"""
u=int(input("input units "))
if u<=100:
    b=u*.40
else:
    if u<=300:
        b=100*.40+(u-100)*.50
    else:
        b=100*.40+200*.50+(u-300)*.60
print("bill=",b)
