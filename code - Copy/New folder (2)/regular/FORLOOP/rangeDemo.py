#range(stop) -> range object | iterable
#range(start,stop,step=1) -> range object | iterable

import time

r=range(10)
print("type is : ",type(r))
print("range object is : ",r) #range(0,10)

for i in r:
    time.sleep(.2)
    print(i)
print("===============")

for i in range(1,21):
    time.sleep(.2)
    print(i)
print("================")

for i in range(2,21,2):
    time.sleep(.2)
    print(i)
print("================")

for i in range(10,0,-1):
    time.sleep(.2)
    print(i)
print("==============")

for i in range(1,10,0): Error arg 3 shouldn't be 0
    time.sleep(.2)
    print(i) 


















