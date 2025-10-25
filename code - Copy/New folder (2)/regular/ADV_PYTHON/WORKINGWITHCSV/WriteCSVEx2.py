
import csv

with open("stu2.csv","w",newline='') as f:
    w=csv.writer(f)
    w.writerow(['sno','sname','scity'])

    while True:
        sno=int(input("Enter sno : "))
        sname=input("Enter sname : ")
        scity=input("Enter scity : ")
        w.writerow([sno,sname,scity])
        opt=input("Do u want another rec y|n ")
        print("===========================")
        if opt in 'Nn':
            break
    
