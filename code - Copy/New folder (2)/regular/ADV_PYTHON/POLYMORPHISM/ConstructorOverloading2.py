import time
class Test:
    def __init__(self,x=None,y=None,z=None):
        time.sleep(.5)
        if x!=None and y!=None and z!=None:
            print("Const with 3 args ",x,y,z)
        elif x!=None and y!=None:
            print("Const with 2 args ",x,y)
        elif x!=None:
            print("Const with 1 args ",x)
        else:
            print("Const with 0 args ")


#calling
t1=Test(10,20,30)
t2=Test(10,20)
t3=Test(10)
t4=Test()
