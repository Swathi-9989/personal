import time

n=int(input("Enter a number : "))  #6
sf=0

for i in range(1,n):
    if n%i==0:
        time.sleep(.2)
        print(i)
        sf=sf+i

print("Perfact" if sf==n else "Not Perfact")

    
