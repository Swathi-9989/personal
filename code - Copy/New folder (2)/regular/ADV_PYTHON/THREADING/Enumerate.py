import time
import threading

def myFun():
    ct=threading.current_thread()
    print(ct.name," started execution ....")
    time.sleep(5)
    print(ct.name," ends execution .... ")

#calling
t1=threading.Thread(target=myFun,name="Child-1  ")
t2=threading.Thread(target=myFun,name="Child-2")
t1.start( )
t2.start( )

nat=threading.active_count()
print("No.of.Active Thread : ",nat)

lst=threading.enumerate()
for t in lst:
    time.sleep(1)
    print(t.name,".....",t.ident)




    









