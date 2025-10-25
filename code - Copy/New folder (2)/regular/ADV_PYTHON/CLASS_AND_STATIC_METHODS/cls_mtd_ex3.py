class Test:
    def method1(self):
        print("Int mtd-1")
        print(self)
        print("=========")

    @classmethod
    def method2(cls):
        print("Cls mtd-2")
        print(cls)

#calling
t=Test()
t.method1()
Test.method2()
