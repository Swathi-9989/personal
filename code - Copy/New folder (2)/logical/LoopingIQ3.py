n=int(input("Enter a number : "))  #3

for i in range(2,n):
    if n%i==0:
        print("Not a prime")
        break
else:
    print("Prime")
        
