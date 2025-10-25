#D.update({k:d})
#D.setdefault(k,d=None)
#D.fromkeys(iterable,value=None) -> dict
#converting string to dict

s="ram=23,nani=34,roja=17"
print("str : ",s)

lst=s.split(",")  #[ram=23,rani=34,roja=17]

stu={}

for i in lst:    
    k,d=i.split("=")  #[ram,23]
    stu.update({k:int(d)})

print("Stu : ",stu)

    
    



