
class Test:
    def __init__(self):
        self.__x=10

class Testing(Test):
    def getData(self):
        #print("Testing private x : ",self.__x)  AE

#calling
t=Testing()
t.getData()
