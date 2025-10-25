#globals( ) -> dict 
x=90 #global

def myFun():
    x=10  #local variable
    print("local x : ",x)
    d=globals()    #{'x':90}
    print("global x : ",d['x'])
    print("global x : ",globals()['x'])
    print("global x : ",d.get('x'))
    print("global x : ",globals().get('x'))
    print("Sum is : ",x+globals().get('x'))
    print("========================")    

#calling
myFun()
