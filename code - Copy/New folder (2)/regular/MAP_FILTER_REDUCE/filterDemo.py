#map(function,*iterable) ->  map | iterable
#list(iterable) | tuple(iterable) | set(iterable) | dict(iterable)

#filter(func or None,iterable) -> filter object | iterable
lst=[2,5,3,6,7,8,9]
print("list : ",lst)
f=list( filter( lambda x: x%2==0 , lst) )
print("Res : ",f)
print("============================")

t=tuple(filter(lambda x: x%3==0 , lst))
print("Result : ",t)
print("=============================")

lst=["ram","anusha","madhu","srijA","sai"]
print("list : ",lst)
t=tuple(filter(lambda x: len(x)==3 , lst))
print("Res : ",t)
print("==============================")

lst=list( filter(lambda x: x[-1] in 'Aa' , lst) )
print("Res : ",lst)






















