
class Test:
    def __init__(self):
        self.x=10 #public

class Testing(Test):
    def getData(self):
        print("public x : ",self.x)

#calling
t=Testing()
t.getData()
