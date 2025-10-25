def SmartDivision(func):
    def wrapper(x,y):
        if y==0:
            print("Sorry V R N D By Zero....")
        else:
            func(x,y)
    return wrapper

@SmartDivision
def division(x,y):
    z=x/y
    print("Result is : ",z)

#calling
a=int(input("Enter a number : "))
b=int(input("Enter b number : "))
division(a,b)
