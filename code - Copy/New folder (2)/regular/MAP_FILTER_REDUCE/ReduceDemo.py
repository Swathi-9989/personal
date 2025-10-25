#map(function,*iterable) ->  map | iterable
#list(iterable) | tuple(iterable) | set(iterable) | dict(iterable)

#filter(func or None,iterable) -> filter object | iterable
#reduce(function,seq)  -> value  | reduce( ) from functools

import functools

r=functools.reduce(lambda x,y: x+y ,[1,2,3,4] )
print("Res : ",r)

f=functools.reduce(lambda x,y : x*y , [1,2,3,4] )
print("Res : ",f)




















