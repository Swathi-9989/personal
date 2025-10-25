#D.update({k:d})
#D.setdefault(k,d=None)
#D.fromkeys(iterable,value=None) -> dict
#converting string to dict

#zip(iterable,iterable) -> zip object | iterable
#D.get(k,d=None) -> d

stu={"sno":101,"sname":"ramesh"}
print("stu : ",stu)

value=stu.get("sname")
print("name is : ",value)

value=stu.get("scity","hyd")
print("city is :",value)

value=stu.get("scity")
print("city is : ",value)




    



