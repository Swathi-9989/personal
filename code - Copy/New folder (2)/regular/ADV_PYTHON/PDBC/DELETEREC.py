import cx_Oracle

conn=cx_Oracle.connect
("scott","Tiger9","localhost:1521/orcl")

if conn!=None:
    print("Connection is Est")

    cur=conn.cursor()
    print("Cursor object is created ")

    empno=int(input("Enter empno : "))
    cur.execute('''DELETE FROM EMP
               WHERE empno=%d''' %empno)

    print(cur.rowcount," Rec are Deleted ....!!!")
    conn.commit()    
    
else:
    print("Connection is Fail ")



