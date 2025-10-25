''' kw-args parameters
        >> If any formal parameters which are declared
             along with **
        >> kw-args can take 0 to n no.of.keyword only
             arguments.
        >> kw-args internally acts as dict collection '''

import time
def myFun(**stu):
    time.sleep(1)
    print("Data is : ",stu)
    for k,d in stu.items():
        time.sleep(.2)
        print(k," >>> ",d)
    print("===================")

#calling
myFun(sno=101,sname="Ramesh",sage=23)
myFun(sno=202,sname="Nani")
myFun(sno=303)
myFun()
         



