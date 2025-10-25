import time

f=open("data3.txt","r")
print("File is closed ? : ",f.closed)
time.sleep(1)

f.close()
print("File is closed ? : ",f.closed)
print("=======================")

with open("data3.txt","r") as f:
    print("inside of with open ")
    time.sleep(1)
    print("File is closed ? : ",f.closed)

time.sleep(1)
print("From outside of with open ")
time.sleep(1)
print("File is closed ? : ",f.closed)





      
