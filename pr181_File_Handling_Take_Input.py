#input employeename and department name and store into emp.dat file
fp=open("emp.dat","w")
en=input("enter empname")
dn=input("enter department")
fp.write(en+"\n")
fp.write(dn+"\n")
fp.close()
print("data stored")
