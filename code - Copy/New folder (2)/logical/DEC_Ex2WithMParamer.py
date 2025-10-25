def Smart_Division(func):
    def wrapper(*arg):
        lst=arg[1: :]
        for i in lst:
            if i==0:
                return "Sorry V R Not D By Zero..."
            else:
                return func(*arg)  #calling func division
    return wrapper            
        
@Smart_Division
def division(a,b):     
    return a/b              

@Smart_Division
def division2(a,b,c):
    return a/b/c

#calling
print("Result : ", division(360,0) )
print("Result : ", division2(360,0,2))

