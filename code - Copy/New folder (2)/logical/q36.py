
def myFun(x):
    print("x : ",x)

#calling
myFun(10)
print("===============")

def myFun(y):
    y[1]=99
    print("Res : ",y)

#calling
lst=[10,20,30]
myFun(lst)
print(lst)
