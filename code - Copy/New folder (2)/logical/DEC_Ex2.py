
def DEC_Split(func):
    def wrapper():
        s=func()
        lst=s.split()
        return lst
    return wrapper

def DEC_Upper(func):   #func is copy of myFun
    def wrapper():
        s=func()        
        return s.upper()
    
    return wrapper


@DEC_Upper #myFun=DEC_Upper(myFun)
@DEC_Split     #myFun=DEC_Split(myFun)
def myFun():
    return "have a nice day dear"

#calling
r=myFun()
print(r)





