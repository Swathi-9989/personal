def myFun():
    print("Fun is invoked ...")
    
class Test:
    def method1(self):
        print("method-1 is invoked ")

#calling
myFun()
#myFun2() NameError

t=Test()
t.method1()
#t.method2() AttributeError


