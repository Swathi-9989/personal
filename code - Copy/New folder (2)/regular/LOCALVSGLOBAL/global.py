x=10

def myFun( ):
    global x
    x=x+90
    print("x val is : ",x)


#calling
myFun( )
print("From outside x : ",x)
