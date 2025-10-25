#L.append(item)
#L.insert(pos,item)
#L.extend(iterable)
#L.copy( ) -> shallow copy of list
#L.pop(index=-1) -> item
#L.remove(item)
#L.clear( )
#L.index(item[,start[,end] ]) -> int
#L.count(item) -> int
#L.reverse( )
#L.sort( ) #After lambda Expression

#       0    1   2    3    4   5 
lst=[10,20,10,50,60,70]
print("list : ",lst)

sno=int(input("Enter an item to be deleted ..."))

for i in lst:
    if i==sno:
        lst.remove(i)

print("After remove : ",lst)









