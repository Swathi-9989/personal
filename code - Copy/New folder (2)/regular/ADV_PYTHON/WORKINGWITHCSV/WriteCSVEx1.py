
import csv

with open("stu1.csv","w") as f:
    w=csv.writer(f)
    w.writerow(['sno','sname','scity'])

print("Data is Saved ")
