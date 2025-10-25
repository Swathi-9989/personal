import threading

def myFun():
    ct=threading.current_thread()
    print(ct.name," started execution ....")
    mt.join( )
    print(ct.name," ends execution ....")

#calling
mt=threading.current_thread()   #main thread
print(mt.name," started execution ....")

t1=threading.Thread(target=myFun,name="Child")
t1.start()
t1.join()
print(mt.name," ends execution .....")
