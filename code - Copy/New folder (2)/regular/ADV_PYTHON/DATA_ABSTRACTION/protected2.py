
class Test:
    def __init__(self):
        self._x=10

class Testing(Test):
    def getData(self):
        print("Test protected x : ",self._x)

#calling
t=Testing()
t.getData( )
