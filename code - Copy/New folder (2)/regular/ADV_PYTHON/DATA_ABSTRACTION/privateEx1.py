
class Test:
    def __init__(self):
        self.__x=10

    def getData(self):
        print("Test private x : ",self.__x)

#calling
t=Test()
t.getData( )
print("From outside of the class")
#print("private x : ",t.__x) AttributError
