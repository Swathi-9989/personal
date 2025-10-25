#s.add(item)
#s.copy( ) -> shallow copy of set
#s.remove(item)   KE
#s.discard(item)
#s.clear( )

#s.union(iterable) -> set   vs
#s.update(iterable) 

a={1,2,3,4}
b={3,4,5,6}
print("set a : ",a)
print("set b : ",b)

# a+b TypeError
c=a.union(b)
print("a union b res c : ",c)
print("==================")

a.update(b)   #a=a.union(b)
print("a update b res a : ",a)







