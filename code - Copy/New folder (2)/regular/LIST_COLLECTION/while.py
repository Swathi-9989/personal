#Ways to read the values from list collection

#unpacking using slicing
#        0        1             2    3   4
lst=[10,"Ramesh",50,60,70]
print("list : ",lst)

#while
import time

index=0
while index<5:
    time.sleep(.2)
    print( lst[index] )
    index=index+1
    

#for
