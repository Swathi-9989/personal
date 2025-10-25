
class Test:
    def method1(self):
        self.x=10  #instance field

#calling
t=Test()
t.method1()
#print("x val is : ",x) NE
print("x val is : ",t.x) #10
