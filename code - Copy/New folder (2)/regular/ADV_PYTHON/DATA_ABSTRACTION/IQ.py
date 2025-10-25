
class Test:
    def __init__(self):
        self.__x=10
        self._y=20
        self.z=30

#calling
t=Test()
print("From outside of the class")
print("private x : ",t._Test__x)
print("protected y : ",t._y)
print("public z : ",t.z)
