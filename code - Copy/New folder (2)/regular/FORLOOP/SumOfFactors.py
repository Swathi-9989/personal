import time

n=int(input("Enter a number : "))

s=0

for i in range(1,n+1):
    time.sleep(.2)
    if n%i==0:
        print(i)
        s=s+i

print("Sum is : ",s)
