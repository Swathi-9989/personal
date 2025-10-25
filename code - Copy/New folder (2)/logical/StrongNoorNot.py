import time
n=int( input("Enter a number : ") )
s=0
temp=n

while n!=0:
    time.sleep(.2)
    r=n%10
    f=1        
    for i in range(1,r+1):
        f=f*i
    s=s+f
    n=n//10
if s==temp:
    print("Strong number")
else:
    porint("Not Strong ")


    

