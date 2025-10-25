''' Rules of constructor
      1.Constructor name must be defined
                with _ _init_ _(self)
      2.Constructor can be parameterized
      3.Constructor never returns any value except None

   Types of constructor
      1.Default constructor or
              0-parameterized constructor
                  or parameterless constructor

      2.Parameterized Constructor
               constructor with parameter.
'''

class Test:
    def __init__(self):
        print("constructor is invoked ")
        self.x=10
        self.y=20

    def getData(self):
        print("x is : ",self.x)
        print("y is : ",self.y)

#calling
t=Test()   #implicitly called by the PVM t.__init__()
t.getData()



















