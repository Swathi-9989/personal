z=30
def OuterFun():
    y=20
    def InnerFun():
        x=10
        print("Inside of InnerFun")
        print("x : ",x)
        print("y : ",y)
        print("z : ",z)
        print("=================")

    InnerFun()
    print("Inside of Outerfun")
    #print("x : ",x)
    print("y : ",y)
    print("z : ",z)
    print("===================")


#From Outside of the OuterFun
OuterFun()
print("From outside of the outer Fun")
#print("x : ",x)
#print("y : ",y)
print("z : ",z)





    




             
