import time

def Shashi():
    yield "Java"
    yield "Oracle"
    yield "Python"

#calling
s=Shashi()
print("Type is : ",type(s))
#print("s : ",s)

for i in s:
    time.sleep(.2)
    print(i)
