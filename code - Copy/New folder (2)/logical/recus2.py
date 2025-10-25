import time

def myFact(n):
    f=1
    if n==0:
        return f
    else:
        f=n*myFact(n-1)

    return f

#calling
r=myFact(3)
print("Res : ",r)
        
        
        
        
