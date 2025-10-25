''' We can pass function as an argument to another
    Function '''

def greet():
    a="Hello "
    return a

def SpecialGreet(func):
    b=func()  #Hello
    c=b+"My Dear"
    return c

#calling
d=SpecialGreet(greet)
print("Res : ",d)
