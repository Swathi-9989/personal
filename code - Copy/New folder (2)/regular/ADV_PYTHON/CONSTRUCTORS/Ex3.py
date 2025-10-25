class Circle:
    def __init__(self,rad):
        self.rad=rad

    def findArea(self):
        area=3.14*self.rad*self.rad
        return area

#calling
r=int(input("Enter radius of circle : "))
c=Circle(r)
ac=c.findArea()
print("Area of Circle : ",ac)

    
