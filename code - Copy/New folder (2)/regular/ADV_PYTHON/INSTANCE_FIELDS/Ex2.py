
class Test:
    def method1(self):
        self.x=10
        print("mtd-1 x ",self.x)

    def method2(self):
        print("mtd-2 x : ",self.x)

#calling
t=Test()
t.method1()
t.method2()
print("instance x : ",t.x)
