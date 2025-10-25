class Mother:
    def color(self):
        print("Color From mother")

class Father:
    def height(self):
        print("height From Father")

class Son(Mother,Father):
    def  job(self):
        print("Job From Son")

#calling
s=Son()
s.color()
s.height()
s.job()
