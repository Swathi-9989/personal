x=10 #int
y=20 #int
z=x+y
print("Sum is : ",z)
print("==================")

a="Sai" #str
b="Baba" #str
c=a+b #str
print("Sum is : ",c)
print("===================")

class Python:
    def __init__(self):
        self.pages=200

class Java:
    def __init__(self):
        self.pages=300

    def __add__(self,other):
        return self.pages+other.pages      
        
#Calling
p=Python()
j=Java()
tp=j+p   # tp=j.__add__(p)
print("Total pages : ",tp)

''' Operator overloading
       >Overriding the predefined magic methods
       existed in the object class.

       > magic methods are the methods which are
       existed in the object class.

       > In Python for every Operator there is a predefined
       method is provided in the object class is called
       magic methods

    +          _ _add_ _(self,other)
    -           _ _sub_ _(self,other)
    *          _ _mul_ _(self,other)
    /          _ _div_ _(self,other)
    //         _ _floordiv_ _(self,other)
    %       _ _mod_ _(self,other)

    >        _ _gt_ _(self,other)
    >=     _ _ge_ _(self,other)
    <       _ _lt_ _(self,other)
    <=    _ _le_ _(self,other)
    ==    _ _eq_ _(self,other)
    !=    _ _ne_ _(self,other)

'''











