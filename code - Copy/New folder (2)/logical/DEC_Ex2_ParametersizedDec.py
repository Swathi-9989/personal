def DEC_Parameter(exp):  #exp is sai
    def DEC_Upper(func):   
        def wrapper():
            s=func()       
            return s.upper() + " Mr|Mrs"+exp
        return wrapper
    return DEC_Upper

@DEC_Parameter(" sai")   
def myFun():                          
    return "Have a nice day "

#calling
'''
inf=DEC_Parameter("sai")  #inf is DEC_Upper()
w=inf(myFun)     #DEC_Upper(myFun)
r=w()
print("Result is : ",r)
'''
print( myFun() )






