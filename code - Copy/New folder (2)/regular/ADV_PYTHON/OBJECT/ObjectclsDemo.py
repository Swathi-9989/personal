import time
import mymodule

e=mymodule.Employee()
print("Module Name is : ",e.__module__)
print("ClassName is : ",e.__class__)
print("DocString : ",e.__doc__)

e.getEmployee()

#Adding new instance field
#e.job='MANAGER'
e.__setattr__('job','MANager')
print( e.__dict__ )

for k,d in e.__dict__.items():
    time.sleep(.2)
    print(k, " >> " ,d)

print("=====================")

#For Updating an existed field
e.__setattr__('job','HOD')
print( e.__dict__ )

#For Reading the value from instance fields
#job=e.job
job=e.__getattribute__('job')
print("Employee job is : ",job)
print("=====================")

#For Deleting an instance field
#del e.job
e.__delattr__('job')
print( e.__dict__ )





























