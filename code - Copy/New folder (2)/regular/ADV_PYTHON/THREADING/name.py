'''Note: whenever u define any thread by
default every thread is created with
default name is thread-1, thread-2.....
Based on the application req, we can set or
get the name of thread by using name attribute '''

import threading

def myFun():
    for i in range(1,11):
        print("myFun ...",i)

#calling
t1=threading.Thread(target=myFun)
print("Thread name is : ",t1.name)
t1.name="Chinni"
print("Thread name is : ",t1.name)
print("============================")

t2=threading.Thread(target=myFun,name="Child")
print("thread name is : ",t2.name)










