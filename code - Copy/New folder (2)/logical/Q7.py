''' Python prg to print set of duplicate values given
in the list '''

lst=[1,2,3,4,4,5,5,6,1]
print("list : ",lst)

lst2=[]
for i in lst:
    if lst.count(i)>1:
        lst2.append(i)

s=set(lst2)
print("Res : ",s)
    
