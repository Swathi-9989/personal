
import threading

def myFun():
    ct=threading.current_thread()
    for i in range(1,11):
        print(ct.name," >>> ",i)

#calling
t1=threading.Thread(target=myFun,name="Child")
t1.start()

for i in range(20,31):
    print("Main .... ",i)
