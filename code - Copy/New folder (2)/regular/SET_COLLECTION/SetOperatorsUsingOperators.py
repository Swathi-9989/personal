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

#s.symmetric_difference(iterable) -> set
#s.symmetric_difference_update(iterable)

a={1,2,3,4}
b={3,4,5,6}
print("set a : ",a)
print("set b : ",b)

c=a|b   #c=a.union(b)
print("a union b res c : ",c)

c=a&b  #c=a.intersection(b)
print("a intersection b res c : ",c)

c=a-b   #c=a.difference(b)
print("a difference b res c : ",c)

c=a^b   #c=a.symmetric_difference(b)
print("a symmetric_difference res c : ",c)












