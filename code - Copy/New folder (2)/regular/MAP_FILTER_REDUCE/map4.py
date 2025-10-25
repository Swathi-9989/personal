#map(function,*iterable) ->  map | iterable
#list(iterable) | tuple(iterable) | set(iterable) | dict(iterable)

lst_rad=[1,2,3,4]
print("list : ",lst_rad)

m=list(map( lambda r: 3.14*r*r , lst_rad) )
print("Map object : ",m)


