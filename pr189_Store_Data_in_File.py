#store two nos into nos.dat file
fp=open("nos.dat","w")
a=input("enter first no.")
b=input("enter second no.")
fp.write(a+"\n")
fp.write(b)
fp.close()
print("data stored")
