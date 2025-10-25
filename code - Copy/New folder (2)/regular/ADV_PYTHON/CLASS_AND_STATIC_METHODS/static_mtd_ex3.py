class Test:
    def method1(x,y,z):
        print("instance method ")
        print("x : ",x)
        print("y : ",y)
        print("z : ",z)
        print("=============")

    @classmethod
    def method2(x,y,z):
        print("class method ")
        print("x : ",x)
        print("y : ",y)
        print("z : ",z)
        print("=============")

    @staticmethod
    def method3(x,y,z):
        print("static method ")
        print("x : ",x)
        print("y : ",y)
        print("z : ",z)
        print("=============")

#calling
t=Test()
t.method1(10,20)
Test.method2(10,20)
Test.method3(10,20,30)











        
        
