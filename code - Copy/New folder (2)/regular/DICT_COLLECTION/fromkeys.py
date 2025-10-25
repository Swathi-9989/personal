#D.update({k:d})
#D.setdefault(k,d=None)

#D.fromkeys(iterable,value=None) -> dict
'''It is used to convert normal collection to the dict
   collection '''

lst=["ram","ramesh","suresh"]
print("list : ",lst)

stu={}
stu=stu.fromkeys(lst)
print("stu : ",stu)
print("======================")

stu2={}
stu2=stu2.fromkeys(lst,"Python")
print("stu2 : ",stu2)







