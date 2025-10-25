import time
#     0       1           2           
t=(10,12.12,"Ramesh")
print("tuple : ",t)

#while
index=0
while index<len(t):
    time.sleep(1)
    print( t[index] )
    index=index+1
    
#for
print("==================")
for i in t:
    time.sleep(.2)
    print(i)






