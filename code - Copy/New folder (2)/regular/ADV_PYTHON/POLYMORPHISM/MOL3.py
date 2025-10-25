
import time
class Math:
    def myAdd(self,*x):
        time.sleep(1)
        print("type is : ",type(x))
        print("Data is : ",x)
        print("Sum is : ",sum(x))   #sum(iterable)
        print("=================")

#calling
m=Math()
m.myAdd(10,20,30,40,50,60)
m.myAdd(10,20,30,40)
m.myAdd(10,20,30)
m.myAdd(10,20)
m.myAdd(10)
m.myAdd()
