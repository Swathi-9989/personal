import time
import sys

print("All command line args ")

for i in sys.argv[1: :]:
    time.sleep(.2)
    print(i)

'''
D:\2025\PYT_APR_830\COMMANDLINEARGS>
      py Ex3.py 10 20 2.2 "shashi kumar" sssit
      
All command line args
10
20
2.2
shashi kumar
sssit
'''


