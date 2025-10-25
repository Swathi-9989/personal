#s.add(item)
#s.copy( ) -> shallow copy of set

a={1,2,3,4}
print("set a : ",a)
b=a.copy()
print("set b : ",b)

a.add("Ramesh")
print("After Modification ")
print("set a : ",a)
print("set b : ",b)
