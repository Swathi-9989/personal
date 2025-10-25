
import time
import csv

with open("stu2.csv","r") as f:
    r=csv.reader(f)
    for lst in r:
        time.sleep(1)
        for i in lst:
            time.sleep(.2)
            print(i,end='\t')
        print(" ")
