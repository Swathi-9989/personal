#s.add(item)
#s.copy( ) -> shallow copy of set
#s.remove(item)   KE
#s.discard(item)
#s.clear( )

#s.union(iterable) -> set   vs
#s.update(iterable)

#s.intersection(iterable) -> set
#s.intersection_update(iterable)

#s.difference(iterable) -> set
#s.difference_update(iterable) 

a={1,2,3,4}
b={3,4,5,6}
print("set a : ",a)
print("set b : ",b)

c=a.difference(b)
print("a difference b res c : ",c)

a.difference_update(b)
print("a difference_update b res a : ",a)












