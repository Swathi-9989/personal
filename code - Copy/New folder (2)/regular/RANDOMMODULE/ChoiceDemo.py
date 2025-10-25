'''choice(seq) -> item '''

import time,random

lst=["java","python","oracle","ds"]
print("list : ",lst)

for i in range(1,11):
    time.sleep(.2)
    print( random.choice(lst) )
