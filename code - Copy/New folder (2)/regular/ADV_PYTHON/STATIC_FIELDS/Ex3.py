
class Test:
    x=10 #static
    def method1(self):
        x=30
        self.x=20 
        print("mtd-1")
        print("local x : ",x)
        print("instance x : ",self.x)
        print("static x : ",Test.x)
        print("===========")

#calling
t=Test()
t.method1()
        
