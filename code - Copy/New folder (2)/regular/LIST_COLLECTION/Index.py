#L.append(item)
#L.insert(pos,item)
#L.extend(iterable)
#L.copy( ) -> shallow copy of list
#L.pop(index=-1) -> item
#L.remove(item)
#L.clear( )
#L.index(item[,start[,end] ]) -> int

#       0    1   2    3    4
lst=[10,20,10,40,50]
print("list : ",lst)

pos=lst.index(10)
print("Index is : ",pos)

pos=lst.index(10,2)
print("Index is : ",pos)

pos=lst.index(10,2,5)
print("Index is : ",pos)








