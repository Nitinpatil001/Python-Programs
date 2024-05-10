#command line arguments
#addition of all command line arguments
import sys
c=0
for i in range(1,len(sys.argv)):
    c=c+int(sys.argv[i])
print(c)
