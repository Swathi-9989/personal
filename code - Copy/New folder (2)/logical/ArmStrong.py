
import time

n=int(input("Enter a number : "))
temp=n
nd=0
s=0

while n!=0:
    time.sleep(.5)
    r=n%10    
    s=s+(r*r*r)
    n=n//10

print("Sum is : ",s)
print("ArmStrng" if s==temp else "Not ArmStrong")
    

    











    
