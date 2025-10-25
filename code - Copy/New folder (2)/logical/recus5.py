#n=3
#1+2+3    or    3+2+1

def sum(n):
    if n==0:
        return 0
    else:
        r=n+sum(n-1)
        return r

#calling
a=sum(5)
print("Sum is : ",a)
