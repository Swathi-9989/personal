
import time

class Test:
    def __init__(self,**stu):
        print("Data is : ",stu)
        for k,d in stu.items():
            time.sleep(.2)
            print(k, " >>> ",d)
        print("===========")

#calling
t1=Test(sno=101,sname="Ramesh",sage=23)
t2=Test(sno=202,sname="Roja")
t3=Test(sno=303)
t4=Test()
