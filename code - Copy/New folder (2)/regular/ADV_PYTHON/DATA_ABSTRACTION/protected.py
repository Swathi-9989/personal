
class Test:
    def __init__(self):
        self._x=10

    def getData(self):
        print("Test protected x : ",self._x)

#calling
t=Test()
t.getData()
