def DEC_Greet(func):   #func is copy of greet
    def wrapper(name):
        if name=="roja":
            print("Hello ",name," Have a Good day ")
        else:
            func(name)
            
    return wrapper

@DEC_Greet   # greet=DEC_Greet(greet)
def greet(name):
    print("Hello ",name," Have a nice day ")

#calling
greet("roja")
