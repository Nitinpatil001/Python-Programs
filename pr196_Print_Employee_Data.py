#read empno name dept and salary from emp.dat file
#and calculate da and hra
fp=open("emp.dat","r")
rn=fp.readline()
nm=fp.readline()
dn=fp.readline()
sal=int(fp.readline())
da=sal*.60
hra=sal*.10
print(da,hra)
fp.close()
