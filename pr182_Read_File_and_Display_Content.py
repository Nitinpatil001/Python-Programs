#read trak file and display its contents
fp=open("trak","r")
for i in fp:
    print(i)
fp.close()
