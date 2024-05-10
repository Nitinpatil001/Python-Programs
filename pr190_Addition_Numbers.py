#read two nos from nos.dat file and print addition
fp=open("nos.dat","r")
a=int(fp.readline())
b=int(fp.readline())
c=a+b
print(c)
fp.close()
