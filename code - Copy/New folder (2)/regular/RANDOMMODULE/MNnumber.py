

''' Random mobile numbers with the following
          total number digits 10 
         1- digit should be 6-9  '''

import time,random

for i in range(1,11):
    time.sleep(.5)
    
    fd=random.randint(6,9)
    sd=""
    for i in range(1,10):
        d=random.randint(0,9)
        sd=sd+str(d)
    mn=str(fd)+sd
    print(mn)


         
         
