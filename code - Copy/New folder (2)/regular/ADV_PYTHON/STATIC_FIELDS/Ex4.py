class Student:
    course="Python" #static

    def setStudent(self):
        self.sno=input("Enter sno : ")
        self.sname=input("Enter sname :  ")

    def getStudent(self):
        print("sno is : ",self.sno)
        print("sname is : ",self.sname)
        print("course is : ",Student.course)

#calling
s1=Student()
s1.setStudent()
s2=Student()
s2.setStudent()

s1.getStudent()
s2.getStudent()









        
