#Remove duplicates from a list without using set().
lst=[1,2,3,4,1,2,4,5,6]
lst2=[]
for i in lst:
    if i not in lst2 :
        lst2.append(i)
print(lst2)

#Find the maximum and minimum elements in a list without using max() and min().

lst3=[]
for i in lst2:
    if i != lst2:
        lst3.append(i)
print(lst3)

