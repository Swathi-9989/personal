import time

def myFun():
    time.sleep(1)
    print("Hello ")
    print("Dear")
    myFun()

#calling
myFun()
