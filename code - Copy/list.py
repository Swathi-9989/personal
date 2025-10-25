
#      0 1 2 3 4 5 6 7
lst=[1,2,3,4,5,6,7,8]
lst.append(9)
print(lst)

print("===========")

l=lst[0:3:]
print(l)

print("============")

lst1=[ ]
lst1.append(lst[7::-1])
print(lst1)

print("==========")

lst=[1,2,3,4,5,6,7,8,22]
count=0
for i in lst:
    count+=1

print("lenght of lst : ",count)
    
    
    
