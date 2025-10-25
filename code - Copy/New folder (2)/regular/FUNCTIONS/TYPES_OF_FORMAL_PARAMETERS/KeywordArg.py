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
myFun(name="Roja",age=23)
myFun(age=23,name="Roja")
#myFun(name="Roja") TypeError








