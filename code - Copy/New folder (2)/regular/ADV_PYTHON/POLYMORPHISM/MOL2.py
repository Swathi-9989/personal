import time

class Math:
    def myAdd(self,x=None,y=None,z=None):
        time.sleep(1)
        if x!=None and y!=None and z!=None:
            s=x+y+z
        elif x!=None and y!=None:
            s=x+y
        elif x!=None:
            s=x
        else:
            s=0
        print("Sum is : ",s)
        print("============================")

#calling
m=Math()
m.myAdd(10,20,30)
m.myAdd(10,20)
m.myAdd(10)
m.myAdd()
