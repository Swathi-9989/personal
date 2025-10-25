import sys
import time

s=0
for i in sys.argv[1 : :]:
    time.sleep(.2)
    print(i)
    s=s+int(i)

print("Sum is : ",s)
