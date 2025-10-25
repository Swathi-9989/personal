import threading

def myFun():
    for i in range(1,11):
        print("myFun... ",i)

def myFun2():
    for i in range(20,31):
        print("myFun2 >>> ",i)

#calling
t1=threading.Thread(target=myFun)
t2=threading.Thread(target=myFun2)
t1.start()
t2.start()
