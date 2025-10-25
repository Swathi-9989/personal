class GF:
    def House(self):
        print("House From GF")

class Father(GF):
    def Car(self):
        print("Car From Father")

class Son(Father):
    def Bike(self):
        print("Bike From Son")

#calling
s=Son()
s.House()
s.Car()
s.Bike()




