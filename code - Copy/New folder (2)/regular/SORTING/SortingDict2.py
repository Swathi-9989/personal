#sorted(iterable,key=None,reverse=False) -> list

import time

stu={"c":"cnu","a":"anu","b":"balu","d":"dhanu"}
print("stu : ",stu)

item=sorted(stu.items()) #[(a,anu),(b,balu),(c,cnu),....]
#print(item)

stu2={}

for k,d in item:
    time.sleep(.2)
    stu2.update({k:d})

print("stu2 : ",stu2)
