import threading,time

def myFun():
    ct=threading.current_thread()
    for i in range(1,11):
        time.sleep(2)
        print(ct.name,".....",i)

#calling
t1=threading.Thread(target=myFun,name="Child")
t1.start()
t1.join()

for i in range(20,31):
    print("Main ....",i)


