
Flat Files :
      The files which are created either by using notepad
      or wordpad
      > In the flat files there is no support for tables
      > Here we can manage the data in the form of columns
         but each column value should be sep by ,
         and these file extension should be .csv
      > These Files are editable in the ms-excel

Steps For Writing the Data into the CSV Files :
=========================================
1.open the file in w mode
        f=open("stu1.csv","w")

2.To write the data into the csv file then we have to use
writerow(iterable) from csv writer class.

3.To Create an object of csv writer class then we have
to call writer(file) func from csv module

                  import csv
                  w=csv.writer(f)
                  
Steps For Reading the Data From CSV Files
=====================================
1.open the file read mode
         f=open("stu1.csv","r")

2.To read the Data from csv File then
we have to use reader class object
from csv module. To Create the Reader class
object then we have to call reader(file) mtd
from csv module.

       import csv
       r=csv.reader(f)

Note: Reader class object is the collection
iterables in the form list type. and Reader
class object is also an iterable.
















         


























        
