''' Positional only arguments
     >> If any formal parameters which are declares
          leftside of / parameter called positional only
          arguments ...

    >> order and count of arguments are matter '''

def myFun(name,age,/):
    print("name is : ",name)
    print("age is : ",age)
    print("=============")

#calling
myFun("Ramesh",23)
#myFun(name="Roja",age=12) TypeError
