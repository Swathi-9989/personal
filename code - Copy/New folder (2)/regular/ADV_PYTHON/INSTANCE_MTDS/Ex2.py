
class Test:
    def method1(self):
        print("Ins mtd-1 of Test")

    def method2(self):
        self.method1()
        print("Ins mtd-2 of Test")

#calliing
t=Test()
t.method2()
