class Test:
    def __init__(self):
        self.x=10
        self.y=20

    def getData(self):
        print("x : ",self.x)
        print("y : ",self.y)

    def __del__(self):
        print("Object is Deleted ....")
        print("Res are DE-Allocated ")    

#calling
t1=Test()
t1.getData( )
t1=None  #del t1
#t1.getData()  AttributeError
print("--------------------")

t2=Test()
print("Data from t2")
t2.getData()




