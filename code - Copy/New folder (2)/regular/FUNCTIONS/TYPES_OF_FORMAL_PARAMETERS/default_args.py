''' default arguments
     >> if we define any formal parameter with some
         value is called default argument.
    >> default arguments are replaced by actual arguments
    >> default arguments are takes place whenever
         we fail to pass the values to formal parameter  '''

def mySum(x=100,y=200,z=300):
    s=x+y+z
    print("Sum is : ",s)
    print("----------------------------")

#calling
mySum(10,20,30)
mySum(10,20)
mySum(10)
mySum()
