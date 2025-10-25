
f=open("data4.txt","r")
l1=f.readline()
print(l1)

l2=f.readline()
print(l2)
f.close()
print("=================")

import time
f=open("data4.txt","r")
lst=f.readlines()
for i in lst:
    time.sleep(.2)
    print(i,end='')

