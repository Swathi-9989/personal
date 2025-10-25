'''Keyword arguments
     >> By default all formal parameters are also acts
          keyword arguments as well
          
     >> In this case we have to pass the values W.R.T
          their names, Here order is not matter but count
          is matter ...   '''

def myFun(name,age):
    print("name is : ",name)
    print("age is : ",age)
    print("===============")

#calling
myFun("Ramesh",23)
myFun(name="Ramesh",age=23)
myFun("Ramesh",age=23)
#myFun(name="Ramesh",23)  SyntaxError








