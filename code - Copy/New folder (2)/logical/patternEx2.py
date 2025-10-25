
import time

n=5
for r in range(n):
    for c in range(r+1):
        time.sleep(.2)
        print("*",end=' ')
    print(" ")
