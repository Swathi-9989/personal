
import time

def myFact(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f

n=int(input("Enter a number : " ))
s=1
f=1
for i in range(2,n+1):
    time.sleep(.2)
    s=s+( 1/myFact(i) )
    print(i,end=' ')
    
print("Result is : ",s)
