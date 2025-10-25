from abc import ABC,abstractmethod

class Test(ABC):
    def method1(self):
        print("Mtd-1 of Test")

    @abstractmethod
    def method2(self):
        pass

#calling
#t=Test() TypeError
