#map(function,*iterable) ->  map | iterable
#list(iterable) | tuple(iterable) | set(iterable) | dict(iterable)

lst=[1,2,3]
print("list : ",lst)
lst2=list(map(lambda x:x*x,lst))
print("Res : ",lst2)
print("===========================")

lst=[1,2,3]
print("list : ",lst)
print("Res : ",list(map(lambda x:x*x,lst)))
    
print("===========================")
print("Res : ",list(map(lambda x:x*x,[1,2,3])))



