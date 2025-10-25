''' Keyword only arguments
         - If any formal parameters which are declared
           rightside of * parameter

         - In this case we have to pass the values W.R.T
         their names only

         - Order is not matter but count is matter .   '''

def myFun(*,name,age):
    print("name is : ",name)
    print("age is : ",age)
    print("===============")

#calling
myFun(name="Ramesh",age=23)
myFun(age=12,name="Chinni")
myFun("Roja",12)









    
