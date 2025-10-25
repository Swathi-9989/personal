#D.keys( ) -> keys | iterable
#D-Dict | k-key | d-value
#D.values( ) -> dict_values | iterable
#D.items( ) -> dict_items | iterable
#dict_items is list of tuples 

import time

stu={"sno":101,"sname":"ramesh","sage":23}
print("stu : ",stu)

items=stu.items()

for t in items:
    time.sleep(.2)
    print(t)
print("================")

for t in items:
    time.sleep(.2)
    k=t[0]
    d=t[1]
    print(k," >>> ",d)
print("================")

for t in items:
    time.sleep(.2)
    k,d=t
    print(k," >>> ",d)
print("====================")

for k,d in items:
    time.sleep(.2)    
    print(k," >>> ",d)



'''
sno >> 101
sname >> ramesh
sage  >> 23 '''



