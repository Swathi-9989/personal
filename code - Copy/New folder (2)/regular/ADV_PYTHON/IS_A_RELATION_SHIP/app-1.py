
class Father:
    def House(self):
        print("House From Father")

class Son(Father):
    def Car(self):
        print("Car from Son")

#calling
s=Son()
s.House()
s.Car()
