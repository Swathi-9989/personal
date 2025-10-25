#sorted(iterable,key=None,reverse=False) -> list
#key=lamda expression | when collection is nested

import time

lst=[("anu",37),("cnu",12),("manu",18),("sudha",26)]
print("list ",lst)

sn=sorted(lst,key=lambda x: x[0])
print(sn)

sa=sorted(lst,key=lambda x : x[1])
print(sa)

print( sa[1] )
