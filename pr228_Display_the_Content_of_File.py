#command line arguments
#display the content of file, given on command line 
import sys
fp=open(sys.argv[1],"r")
for i in fp:
    print(i)
