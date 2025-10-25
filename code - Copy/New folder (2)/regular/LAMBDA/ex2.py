#Defining the function
def add(x,y):
    s=x+y
    return s

#calling
r=add(10,20)
print("Result is : ",r)
print("======================")

myAdd=lambda x,y: x+y
a=int(input("Enter a number : "))
b=int(input("Enter b number : "))
r2=myAdd(a,b)
print("Result is : ",r2)


