
import threading

def myFun():
    ct=threading.current_thread()
    print(ct.name," started execution....!!! ")

#calling
t1=threading.Thread(target=myFun,name="Child-1")
t2=threading.Thread(target=myFun,name="Child-2")
t1.start( )
t2.start()
