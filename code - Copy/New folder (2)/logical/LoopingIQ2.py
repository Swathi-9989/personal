'''

  for vari in <iterable>:
  .... stmt(s)
  else:
  .... stmt(s)

  while <condition>:
  ....stmt(s)
  else:
  ....stmt(s)
  
'''
import time
i=1
while i<=5:
    time.sleep(.5)
    print("Hello ...",i)
    if i==3:
        break    
    i=i+1
else:
    print("Nice")

print("For .....")
import sys
for i in range(1,6):
    time.sleep(.5)
    print("Hello ....",i)
    if i==4:
        sys.exit()
else:
    print("Nice" )











