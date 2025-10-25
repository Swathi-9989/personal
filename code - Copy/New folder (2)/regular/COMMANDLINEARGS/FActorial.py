import math
import time,sys

n=int(sys.argv[1])  #5
f=1

for i in range(1,n+1):
    time.sleep(.2)
    print(i)
    f=f*i
print("Fact is : ",f)

print("Factorial ",math.factorial(n))
    
