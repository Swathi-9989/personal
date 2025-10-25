
class Test:
    def __init__(self):
        print("Const is invoked ")

    def __del__(self):
        print("Dest is invoked ")

#calling
lst=[Test(),Test(),Test()]
#lst[1]=None
del lst
