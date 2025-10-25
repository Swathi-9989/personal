class Test:
    x=10 #static variable
    
    def method1(self):
        self.y=20 #instance
        print("instance y : ",self.y)
        print("static x : ",Test.x)
        print("==================")

    @classmethod
    def method2(cls):
        print("cls mtd")
        print("static x : ",Test.x)
        print("static x : ",cls.x)        

#calling
t=Test()
t.method1()
Test.method2()

        
