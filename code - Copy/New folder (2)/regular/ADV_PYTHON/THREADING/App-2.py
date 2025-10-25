import threading

class Test:
    def method1(self):
        for i in range(1,11):
            print("mtd-1 ... ",i)

    def method2(self):
        for i in range(20,31):
            print("mtd-2 >>> ",i)

#calling
t=Test()
t1=threading.Thread(target=t.method1)
t2=threading.Thread(target=t.method2)
t1.start()
t2.start()
