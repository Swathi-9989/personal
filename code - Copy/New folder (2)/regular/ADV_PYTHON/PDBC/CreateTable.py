
import cx_Oracle

conn=cx_Oracle.connect
("scott","Tiger9","localhost:1521/orcl")

if conn!=None:
    print("Connection is Est")

    cur=conn.cursor()
    print("Cursor object is created ")

    query=''' CREATE TABLE MASTINFO
                             (sno number(3),sname varchar(10),
                              scity varchar(10) )'''
    cur.execute(query)
    print("Table is created ")

    cur.close()
    conn.close()
    
else:
    print("Connection is Fail")


