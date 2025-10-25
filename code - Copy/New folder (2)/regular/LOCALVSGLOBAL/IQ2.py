
def OuterFun():
    x=10
    def InnerFun():
        nonlocal x
        x=x+20
        print("Inside of the inner Fun x : ",x)

    InnerFun()
    print("Inside of outer Fun x : ",x)

#calling
OuterFun()
