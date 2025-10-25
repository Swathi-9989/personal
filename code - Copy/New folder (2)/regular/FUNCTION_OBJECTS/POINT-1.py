'''  We can assign function object to a variable '''

def greet():
    print("Hello")

#calling
print("type is : ",type(greet))
print("HC :",greet)
greet()
print("=========================")

x=greet
print("type is : ",type(x))
print("HC:",x)
x()
