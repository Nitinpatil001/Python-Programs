#read all rollno,name,mar,hin,eng from stud.dat file and print the result
fp=open("stud.dat","r")
while True:
    rn=fp.readline()
    if rn=="":
       break
    nm=fp.readline()
    m=int(fp.readline())
    h=int(fp.readline())
    e=int(fp.readline())
    t=m+h+e
    p=t*100/300
    if p<40:
        rm="fail"
    elif p<50:
        rm="pass class"
    elif p<60:
        rm="second class"
    elif p<70:
        rm="first class"
    else:
        rm="distinction"
    print("rollno=",rn)
    print("name=",nm)
    print("marathi",m)
    print("hindi",h)
    print("english",e)
    print("total",t)
    print("percent",p)
    print("remark",rm)
