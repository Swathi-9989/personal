class Employee:
    def setEmployee(self):
        self.eno=input("Enter eno : ")
        self.ename=input("Enter ename : ")
        self.d=self.Doj()
        self.d.setDoj()        

    def getEmployee(self):
        print("eno is : ",self.eno)
        print("ename is : ",self.ename)
        self.d.getDoj()

    class Doj:
        def setDoj(self):
            self.dd=input("Enter dd : ")
            self.mm=input("Enter mm :")
            self.yy=input("Enter yy : ")

        def getDoj(self):
            print(f"Doj is {self.dd}-{self.mm}-{self.yy}")

#Calling
e=Employee()
e.setEmployee()
e.getEmployee()









