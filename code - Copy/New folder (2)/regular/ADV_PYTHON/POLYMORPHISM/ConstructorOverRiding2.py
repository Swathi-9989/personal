
class Test:
    def __init__(self):
        print("Const of Test")

class Testing(Test):
    def __init__(self):
        super().__init__()     #super().__init__([args])
        print("Const of Testing")

#calling
t=Testing()
