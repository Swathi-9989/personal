''' Accept 3 subject from the user
findout Result
     print Pass if marks > 34 in all subjects else Fail
'''

m1=int(input("Enter m1 : "))  # 40
m2=int(input("Enter m2 : "))  # 50
m3=int(input("Enter m3 : "))  # 60

if m1>34 and m2>34 and m3>34:
    print("Result is : Pass")
else:
    print("Result is : Fail ")
