''' Accept a number findout no.of.digits in the given
number '''

n=input("Enter a number ")  #12345  | str
no=len(n)
print("No.of.Digits : ",no)
print("===============================")

import time

n=int(input("Enter a number : "))
nd=0

while n!=0:
    time.sleep(1)    
    r=n%10    
    nd=nd+1
    n=n//10

print("no.of.Digits : ",nd)










    
