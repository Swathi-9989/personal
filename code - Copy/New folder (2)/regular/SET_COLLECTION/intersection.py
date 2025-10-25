#s.add(item)
#s.copy( ) -> shallow copy of set
#s.remove(item)   KE
#s.discard(item)
#s.clear( )

#s.union(iterable) -> set   vs
#s.update(iterable)

#s.intersection(iterable) -> set
#s.intersection_update(iterable)

a={1,2,3,4}
b={3,4,5,6}
print("set a : ",a)
print("set b : ",b)

c=a.intersection(b)  # {3,4}
print("a intersection b res c : ",c)

a.intersection_update(b)
print("a intersection_update res a : ",a)





