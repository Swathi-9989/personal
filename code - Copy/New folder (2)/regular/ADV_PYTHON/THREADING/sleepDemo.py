'''
   How to delay the execution of thread till the specified
   time in seconds
   Ans: by using sleep( ) from time module.
'''

import threading,time

def myFun():
    #time.sleep(5)
    ct=threading.current_thread()
    for i in range(1,11):
        print(ct.name,"....",i)

#calling
t1=threading.Thread(target=myFun,name="child")
t1.start()

time.sleep(5)
for i in range(20,31):
    print("main >>> ",i)







