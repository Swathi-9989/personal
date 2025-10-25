#map(function,*iterable) ->  map | iterable
#list(iterable) | tuple(iterable) | set(iterable) | dict(iterable)

#filter(func or None,iterable) -> filter object | iterable

lst=[12,0,3.3,0.0,False,0+0j,12+123j,"","Roja"]
print("list:",lst)

t=tuple(filter( None ,lst))
print("Result is : ",t)




















