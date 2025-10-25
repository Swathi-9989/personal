def DEC_Upper(func):   #func is copy of myFun
    def wrapper():
        s=func()
        s=s.upper()
        return s

    return wrapper

def myFun():
    return "have a nice day dear"

#calling
inf=DEC_Upper(myFun)   #inf is wrapper
r=inf()
print(r)
