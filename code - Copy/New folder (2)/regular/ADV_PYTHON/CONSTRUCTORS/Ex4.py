class Triangle:
    def __init__(self,b,h):
        self.b=b
        self.h=h

    def findArea(self):
        return 0.5*self.b*self.h

#calling
t=Triangle(5,5)
at=t.findArea()
print("Area of Triangle : ",at)
