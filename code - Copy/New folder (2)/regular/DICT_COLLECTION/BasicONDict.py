stu={}
print("stu : ",stu)

#Adding new item to dict
stu['sname']='Roja'
stu['sage']=29
print("Stu : ",stu)
print("====================")

#For Updating an existed item
stu['sname']='Sudha'
print("After update : ",stu)
print("====================")

#For Reading the value
na=stu['sname']
print("Name is : ",na)

#city=stu['scity'] KeyError
#For deleting an item
del stu['sname']
print("stu : ",stu)



