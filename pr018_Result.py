"""input rollno,name and marks of marathi,hindi,and english
and print total percentage and remark """
rn=int(input("enter rollno"))
nm=input("enter name ")
m=int(input("enter marathi "))
h=int(input("enter hindi "))
e=int(input("enter english "))
t=m+h+e
p=t*100/300
if p<40:
    rm="fail"
else:
    if p<50:
        rm="pass class"
    else:
        if p<60:
            rm="second class"
        else:
            if p<70:
                rm="first class"
            else:
                rm="distinction"
print("Total marks = ",t)
print("Percentage = ",p)
print("Ramark = ",rm)
