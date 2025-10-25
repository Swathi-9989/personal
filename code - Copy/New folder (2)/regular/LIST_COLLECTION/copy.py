#L.append(item)
#L.insert(pos,item)
#L.extend(iterable)
#L.copy( ) -> shallow copy of list
#L.pop(index=-1) -> item

#       0    1   2    3    4
lst=[10,20,30,40,50]
print("list : ",lst)

item=lst.pop()   #defualt index is -1 thus last item is del
print("Deleted item : ",item)

item=lst.pop(2)
print("Deleted item : ",item)
print("list : ",lst)

