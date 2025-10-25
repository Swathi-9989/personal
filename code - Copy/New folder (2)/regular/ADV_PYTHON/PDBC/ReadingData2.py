import cx_Oracle
import time

conn=cx_Oracle.
connect("scott","Tiger9","localhost:1521/orcl")

if conn!=None:
    print("Connection is Est ")

    cur=conn.cursor()
    print("Cursor object is created ")

    cur.execute(''' SELECT empno,ename,job from emp''')
    lst=cur.fetchmany(3)

    for t in lst:
        time.sleep(.2)
        for i in t:
            time.sleep(.2)
            print(i,end='\t')
        print(" ")

    cur.close()
    conn.close()
    
else:
    print("Connection is Fail ")



