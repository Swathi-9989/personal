
class Test:
    x=10 #static
    def method1(self):
        print("mtd-1")
        print("x : ",self.x)
        print("x : ",Test.x)
        print("===========")

#calling
t=Test()
t.method1()
        
