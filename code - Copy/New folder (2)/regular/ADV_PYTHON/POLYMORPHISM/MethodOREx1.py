
'''
Method overriding
   > Process of defining sub class method same as
      super class method called method overriding
      
   > In this case priority is given to the
      sub class mtd only

  IQ: When do we go for method overridig ?
  Ans: Whenever u want use the super class method
  into the sub class with different implementation. '''

class Test:
    def method1(self):
        print("Mtd-1 of Test")

class Testing(Test):
    pass

#calling
t=Testing()
t.method1()










