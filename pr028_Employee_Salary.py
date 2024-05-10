"""
input designation and basic of employee and calculate the DA(Dearness
Allownce) and HRA(House Rent Allownce) as followes
for manager da is 60% of basic and hra is 10% of basic
for clerk da is 50% of basic and hra is 5% of basic
for peon da is 40% of basic and hra is 4% of basic
print the da and hra
"""
d=input("input designation ")
b=int(input("input basic "))
if d=="manager":
    da=b*.60
    hra=b*.10
elif d=="clerk":
    da=b*.50
    hra=b*.05
elif d=="peon":
    da=b*.40
    hra=b*.04
else:
    da=0
    hra=0
print(da,hra)
