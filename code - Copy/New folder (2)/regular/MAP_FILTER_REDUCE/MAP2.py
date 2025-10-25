#map(function,*iterable) ->  map | iterable
#list(iterable) | tuple(iterable) | set(iterable) | dict(iterable)

lst=[1,2,3]
print("list : ",lst)

m=map(lambda x:x*x,lst)

lst2=list(m)
print("Res : ",lst2)
    
    
