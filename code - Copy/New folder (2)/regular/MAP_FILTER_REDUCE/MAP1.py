#map(function,*iterable) ->  map | iterable

lst=[1,2,3]
print("list : ",lst)

def sq(x):
    s=x*x
    return s

#calling
lst2=[]
for i in lst:
    r=sq(i)
    lst2.append(r)

print("Res : ",lst2)
    
    
