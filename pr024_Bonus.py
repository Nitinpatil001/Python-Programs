"""
input code and basic of employee and calculate the bonus as
for 1st employee code bonus is 15% of basic
for 2nd employee code bonus is 17% of basic
for 3rd employee code bonus is 1000 rs.
print the bonus
"""
c=int(input("employee code "))
b=int(input("employee basic "))
if c==1:
    bo=b*.15
else:
    if c==2:
        bo=b*.17
    else:
        if c==3:
            bo=1000
        else:
            bo=0;
print("code=",c,"basic=",b,"bonus=",bo)
