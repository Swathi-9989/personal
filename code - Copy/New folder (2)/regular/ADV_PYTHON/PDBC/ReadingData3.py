import cx_Oracle
import time

conn=cx_Oracle.
connect("scott","Tiger9","localhost:1521/orcl")

if conn!=None:
    #print("connection is Est")
    
    cur=conn.cursor()
    #print("Cursor object is created ")

    cur.execute('''SELECT empno,ename,job
           From emp ''')

    lst=cur.fetchall()

    for t in lst:
        time.sleep(.2)
        for i in t:
            time.sleep(.2)
            print(i,end='\t')
        print(" ")
        
else:
    print("Connection is Fail")

    
