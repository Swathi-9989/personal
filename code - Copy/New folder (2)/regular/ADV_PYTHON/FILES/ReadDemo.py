#read( ) -> str
import time

f=open("data3.txt","r")
data=f.read()

for i in data:
    time.sleep(.02)
    print(i,end='')

pos=f.tell()
print("\niam @ : ",pos)

f.seek(0)
pos=f.tell()
print("\niam @ : ",pos)

data=f.read(7)
print("Data is : ",data)    
f.close()



