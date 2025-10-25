import cx_Oracle

conn=cx_Oracle.
connect("scott","Tiger9","localhost:1521/orcl")

if conn!=None:
    print("Connection is Est ")

    cur=conn.cursor()
    print("Cursor object is created ")

    query='''UPDATE EMP SET SAL=SAL+%d,
        COMM=COMM+%d WHERE job='%s'  '''

    inc_sal=int(input("Enter inc_salary : "))
    inc_comm=int(input("Enter inc_comm : "))
    job_title=input("Enter job_title : ")
    
    cur.execute(query  %(inc_sal,inc_comm,job_title))
    conn.commit()
    print(cur.rowcount," Rec are inserted ....")

    cur.close()
    conn.close()
    
else:
    print("Connection is Fail ")


