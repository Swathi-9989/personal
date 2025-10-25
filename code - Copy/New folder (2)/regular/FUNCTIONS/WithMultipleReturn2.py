#defining 
def myCalc(x,y):
    a=x+y  #12
    s=x-y   #8
    m=x*y #20
    return a,s,m

#calling
t=myCalc(10,2)           #t=12,8,20   packing | tuple
print("Add is : ",t[0])
print("Sub is : ",t[1])
print("Mul is : ", t[2])

