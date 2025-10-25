'''Given a string like "swiss",
find the first character that doesn’t repeat.
The answer here is "w". '''

#App-1
import collections

data="swiss"
print("Data is : ",data)
res=collections.Counter(data)
print(res)
for k,d in res.items():
    if d==1:
        print(k)
        break
print("======================")

#App-2
data="swiss"
res={}
for i in data:
    res[i]=res.get(i,0)+1  #{'s':3,'w':1,'i':1}

for k in res:
    if res[k]==1:
        print(k)
        break
print("====================")
