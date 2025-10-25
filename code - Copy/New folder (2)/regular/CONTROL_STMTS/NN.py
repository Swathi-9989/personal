
import time

s=0
i=1
while i<=5:
    time.sleep(.2)
    print(i)
    s=s+i
    i=i+1

print("Sum is : ",s)
