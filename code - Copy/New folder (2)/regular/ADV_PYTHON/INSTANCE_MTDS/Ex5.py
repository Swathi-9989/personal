class Circle:
    def setRadius(self,rad):
        self.rad=rad

    def findArea(self):
        return 3.14*self.rad*self.rad

#calling
c=Circle()
r=int(input("Enter radius of circle : "))
c.setRadius(r)
ac=c.findArea( )
print("Area of Circle : ",ac)
