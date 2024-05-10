#read myinfo.dat file and display its contents
fp=open("myinfo.dat","r")
for i in fp:
    print(i)
fp.close()
