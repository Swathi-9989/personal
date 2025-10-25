
class Employee:
    def __init__(self):
        self.ename=input("Enter ename : ")
        self.spd=int(input("Enter sal per day : "))

    def __mul__(self,other):
        return self.spd*other.dw    

class TimeSheet:
    def __init__(self):
        self.dw=int(input("Enter Days worked : "))

    def __mul__(self,other):
        return self.dw*other.spd

#calling
e=Employee()
t=TimeSheet()
ns=e*t  #e.__mul__(t)
print("Netsalary is : ",ns)



