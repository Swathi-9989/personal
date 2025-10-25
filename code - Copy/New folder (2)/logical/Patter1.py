
import time

n=5
for i in range(n):
    for j in range(i,n):
        time.sleep(.2)
        print(" ",end=' ')

    for k in range(i+1):
        print("*",end=' ')
        
    print(" ")
