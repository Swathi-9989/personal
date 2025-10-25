#D.update({k:d})
#D.setdefault(k,d=None)
#D.fromkeys(iterable,value=None) -> dict

#converting string to dict
s="ram nani roja"
print("str : ",s)

#str.split([chars]) -> list
#convert that list to dict by using fromkeys

lst=s.split()  #[ram,nani,roja]
stu={}
stu=stu.fromkeys(lst)
print("Stu : ",stu)




