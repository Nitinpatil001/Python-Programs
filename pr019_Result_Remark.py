"""input rollno,name and marks of marathi,hindi,and english
and print total percentage and remark """
rn=int(input("enter rollno"))
nm=input("enter name ")
m=int(input("enter marathi "))
h=int(input("enter hindi "))
e=int(input("enter english "))
t=m+h+e
p=t*100/300
print(t,p)
if p<40:
    print("fail")
else:
    if p<50:
        print("pass class")
    else:
        if p<60:
            print("second class")
        else:
            if p<70:
                print("first class")
            else:
                print("distinction")
