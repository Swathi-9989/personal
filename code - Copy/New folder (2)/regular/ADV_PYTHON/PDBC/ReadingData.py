import cx_Oracle

conn=cx_Oracle.
connect("scott","Tiger9","localhost:1521/orcl")

if conn!=None:
    print("Connection is Est")

    cur=conn.cursor()
    print("Cursor object is created ")

    cur.execute('''select empno,ename,job from emp''')
    t=cur.fetchone()

    print("Empno : ",t[0])
    print("Ename is : ",t[1])
    print("Ejob is : ",t[2])

    cur.close()
    conn.close()
    
else:
    print("Connection is Fail ")
    
