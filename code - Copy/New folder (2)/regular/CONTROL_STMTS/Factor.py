
import time

n=int(input("Enter no : "))

f=1
i=1
while i<=n:
    time.sleep(.2)
    print(i)
    f=f*i
    i=i+1

print("Fact is : ",f)
