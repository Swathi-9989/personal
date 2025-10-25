#D.update({k:d})
#D.setdefault(k,d=None)
#D.fromkeys(iterable,value=None) -> dict
#converting string to dict

#       0           1            2
a=["mani","nani","raj"]
b=[34,45,56]

stu={}

for i in range(3):
    key=a[i]
    value=b[i]
    stu.update({key:value})

print("stu : ",stu)
    

    



