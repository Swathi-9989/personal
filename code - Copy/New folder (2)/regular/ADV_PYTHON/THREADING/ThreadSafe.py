import threading
import time

class ATM:
    def __init__(self):
        self.l=threading.Lock()
        
    def wd(self,name):
        self.l.acquire()
        for i in range(1,11):
            time.sleep(.2)
            print("WD By Mr|Mrs ",name)
        self.l.release()

#calling
a=ATM()
t1=threading.Thread(target=a.wd,args=("Ramesh",))
t2=threading.Thread(target=a.wd,args=("Suresh",))
t1.start()
t2.start()
