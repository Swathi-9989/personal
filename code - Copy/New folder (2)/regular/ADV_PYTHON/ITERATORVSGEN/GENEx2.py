import time

for i in range(1,10):
    time.sleep(.2)
    print(i)
print("=============")

def myRange(start,stop,step=1):
    while start<=stop:
        yield start
        start=start+step

for i in myRange(1,10,2):
    time.sleep(.2)
    print(i)
