
class Test:
    @classmethod
    def method1(cls):
        print("cls mtd-1 of Test")

#calling
t=Test()
t.method1()
Test.method1()
