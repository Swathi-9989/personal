
def findArea(l,b):
    a=l*b
    return a

#calling
ar=findArea(5,5)
print("Area of Rect : ",ar)
print("===============")

ar=lambda l,b: l*b
ar2=ar(5,5)
print("Area of Rect : ",ar2)



