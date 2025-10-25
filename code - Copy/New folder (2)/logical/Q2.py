''' count the frequency of each char '''

#App-1
s="hello"
res={}
for i in s:
    res[i]=res.get(i,0)+1  #{"h":1,"e":1,"l":2,"o":1}
print("Res : ",res)
print("======================")

#App-2
import collections
#Counter(iterable) -> dict 
res2=collections.Counter(s)
print(res2)

import time
for k,d in res2.items():
    time.sleep(.2)
    print(k," >>> ",d)
    







    





