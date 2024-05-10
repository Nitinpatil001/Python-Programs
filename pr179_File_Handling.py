#file handling
#store yourname,addr and city into "myinfo.dat" file
fp=open("myinfo.dat","w")
fp.write("ssvps\n")
fp.write("deopur\n")
fp.write("dhule\n")
fp.close()
print("information stored")
