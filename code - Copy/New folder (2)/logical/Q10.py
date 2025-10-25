lst=[1,1,2,3,4,4,5,6,5]
print("list : ",lst)
lst2=[]

for i in lst:
    if lst.count(i)==1:
        lst2.append(i)

print("Res : ",lst2)

#App-2
#[<exp> for <var> in iterable if test ] -> list
lst3=[i for i in lst if lst.count(i)==1]
print("Res : ",lst3)


    
