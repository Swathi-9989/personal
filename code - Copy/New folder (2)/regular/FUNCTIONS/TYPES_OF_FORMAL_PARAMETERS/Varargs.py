''' Varargs [ Variable length args ]
     >> process of defining the formal parameter with *
     >> varargs can take 0 to n no.of.positional only args
     >> internally varargs acts as tuple collection '''

import time

def mySum(*x):
    time.sleep(1)
    print("Type is : ",type(x))
    print("Data is : ",x)
    print("Sum is : ",sum(x))    #sum(iterable)
    print("==================")

#calling
mySum(10,20,30,40,50,60)
mySum(10,20,30,40)
mySum(10,20)
mySum(10)
mySum()





    
