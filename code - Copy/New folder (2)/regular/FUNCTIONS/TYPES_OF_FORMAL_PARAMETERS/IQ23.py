def myFun(*x,*y):    #invalid 
    pass

#calling
myFun(10,20,30,40)

def myFun2(**x,**y):    #invalid 
    pass

#calling
myFun(sno=101,sname="Roja")

def myFun3(*x,**y):  #valid
    pass

#calling
myFun3(10,20,30,40,50,sno=101,sname="Ram")
