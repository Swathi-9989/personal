

import sys
import time

s=0
for i in sys.argv[1 : :]:
    time.sleep(.2)
    print(i)
    s=s+int(i)

print("Sum is : ",s)

'''
D:\2025\PYT_APR_830\COMMANDLINEARGS>
          py SumAll.py 10 20 30 40 50 60
10
20
30
40
50
60
Sum is :  210  '''
