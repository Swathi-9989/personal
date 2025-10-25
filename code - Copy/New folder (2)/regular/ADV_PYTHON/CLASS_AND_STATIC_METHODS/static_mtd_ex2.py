class Test:
    @staticmethod
    def method1():
        print("static mtd-1")

    def method2(self):
        self.method1()
        Test.method1()
        print("Ins mtd-2")

#calling
t=Test()
t.method2()
