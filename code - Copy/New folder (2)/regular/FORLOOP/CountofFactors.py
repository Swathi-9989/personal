
import time

n=int( input("Enter a number : ") )
cnt=0

for i in range(1,n+1):
    time.sleep(.2)
    if n%i==0:
        print(i)
        cnt=cnt+1

print("Count is : ",cnt)
