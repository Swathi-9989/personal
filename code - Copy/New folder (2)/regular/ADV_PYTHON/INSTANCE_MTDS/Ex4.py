class Test:
    def setData(self,x,y):
        self.x=x
        self.y=y

    def findBiggest(self):
        if self.x>self.y:
            print("Biggest is : ",self.x)
        else:
            print("Biggest is : ",self.y)

#calling
t=Test()
t.setData(10,20)
t.findBiggest()
