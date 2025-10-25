
class Test:
    def __init__(self):
        print("Const is invoked ")

    def __del__(self):
        print("Dest is invoked ")

#calling
t1=Test()
t2=t1
t3=t2
t3=None
t2=None
t1=None
