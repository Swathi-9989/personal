

#range(start,stop,step=1) -> range object
#randrange(start,stop,step=1) -> value


import time
import random

for i in range(1,11):
    time.sleep(.2)
    print( random.randrange(2,20,2) )
    
