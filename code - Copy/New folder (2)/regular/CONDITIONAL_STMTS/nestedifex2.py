''' Accept 3 subject marks ,calculate total,
avg , Result and Grade

     Result is :  pass iff marks > 34 in all subjects else Fail
     Note : If Result is pass then check the avg marks
                        if avg >=70 print Grade A
                        if avg>=60  print Grade B
                        if avg>=50  print Grade C else Grade-D '''

m1=int(input("Enter m1 : "))
m2=int(input("Enter m2 : "))
m3=int(input("Enter m3 : "))

tot=m1+m2+m3
avg=tot/3

print("total is : ",tot)
print("avg is : ",avg)

if m1>34 and m2>34 and m3>34:
    print("Result is Pass ")
    if avg>=70:
        print("Grade-A")
    elif avg>=60:
        print("Grade-B")
    elif avg>=50:
        print("Grade-C")
    else:
        print("Grade-D")
else:
    print("Result is Fail ")


                    



