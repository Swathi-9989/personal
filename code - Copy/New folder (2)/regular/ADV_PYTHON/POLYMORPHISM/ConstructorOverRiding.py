
'''
   Constructor overriding
       >  constructors are inherited
       >  process of defining the sub class constructor
           same as super class constructor           
'''

class Test:
    def __init__(self):
        print("Const of Test")

class Testing(Test):
    pass

#calling
t=Testing()
