from abc import ABC,abstractmethod

class Test(ABC):
    def method1(self):
        print("mtd-1 of Test")

#calling
t=Test()
t.method1()
