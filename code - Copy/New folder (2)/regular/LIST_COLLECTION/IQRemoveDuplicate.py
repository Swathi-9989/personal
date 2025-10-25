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

a=[10,20,10,50,10,70]
print("list : ",a)

b=[]  #10,20

for i in a:
    if i not in b:
        b.append(i)

print("list b : ",b)







