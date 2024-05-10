#store rollno name and marks of marathi,hindi and english into stud.dat file
fp=open("stud.dat","a")
ch='y'
while ch=='y':
    rn=input("enter rollno")
    nm=input("enter name")
    mr=input("enter marathi marks")
    hn=input("enter hindi marks")
    en=input("enter english marks")
    fp.write(rn+"\n")
    fp.write(nm+"\n")
    fp.write(mr+"\n")
    fp.write(hn+"\n")
    fp.write(en+"\n")
    ch=input("continue(y/n)")
    
fp.close()
print("data stored")
