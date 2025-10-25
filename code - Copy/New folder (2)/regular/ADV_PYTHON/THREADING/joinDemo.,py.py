
import threading,time

def myFun():
    ct=threading.current_thread()
    for i in range(1,11):
        print(ct.name,".....",i)

#calling
t1=threading.Thread(target=myFun,name="Child")
t1.start()

for i in range(20,31):
    time.sleep(.2)
    print("Main ....",i)


