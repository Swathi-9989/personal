import time

n=5

for r in range(5):
    for c in range(r+1):
        time.sleep(.2)
        print(" ",end=' ')

    for k in range(r,n-1):
        time.sleep(.2)
        print("*",end=' ')

    for k in range(r,n):
        time.sleep(.2)
        print("*",end=' ')
        
    print()
