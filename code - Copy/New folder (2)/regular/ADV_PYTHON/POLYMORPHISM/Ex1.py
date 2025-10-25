
class Test:
    def method1(self):
        print("Mtd-1 wout arg ")

    def method1(self,x):
        print("mtd-1 with 1-arg ",x)

#calling
t=Test()
t.method1(123)
#t.method1() TypeError

        
