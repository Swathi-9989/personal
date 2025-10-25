'''Note: Whenever a thread is started execution
then status of the thread is running state. But whenever
thread is complited its execution then the status of
thread becomes dead state.

is_alive() mtd from threading module '''
import threading,time

def myFun():
    ct=threading.current_thread()
    print(ct.name, " started execution .... ")
    time.sleep(5)
    print(ct.name, " ends execution .....")

#calling
t1=threading.Thread(target=myFun,name="Child")
t1.start()

print("Thread t1 is_alive ? : ",t1.is_alive())
time.sleep(10)
print("thread t1 is_alive ? : ",t1.is_alive())













