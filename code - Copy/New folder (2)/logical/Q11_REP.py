
lst=[1,1,2,3,4,4,5,6,5]
print("list : ",lst)
lst2=[]

#App1
for i in lst:
    if lst.count(i)>1:
        lst2.append(i)

s=set(lst2)
print("s : ",s)


    


    
