
stu={"sno":101,"sname":"ramesh","sage":23}
print("stu : ",stu)

key=input("Enter key : ")  #sno

try:
    value=stu[key] #sno
except KeyError:
    print("KE : Sorry Invalid key ")
else:
    print("Value of the given key : ",value)
