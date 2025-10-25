

stu={}

for i in range(1,3):
    lst=[]
    name=input("Enter name : ")
    mobile=input("Enter mobile : ")
    city=input("Enter city ")
    lst.append([mobile,city])    
    stu[name]=lst

sname="sai"
for k,d in stu.items():
    if d[0]==sname:
        print(d)
        break
    
print(stu)

    
