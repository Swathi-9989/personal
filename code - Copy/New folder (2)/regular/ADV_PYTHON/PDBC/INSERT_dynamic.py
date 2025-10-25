import cx_Oracle

conn=cx_Oracle.
connect("scott","Tiger9","localhost:1521/orcl")

if conn!=None:
    print("Connection is Est")

    cur=conn.cursor()
    print("Cursor object is created ")

    sno=int(input("Enter sno : "))
    sname = input("Enter sname : ")
    scity=input("Enter scity : ")
    
    cur.execute('''INSERT INTO MASTINFO
        VALUES(%d,'%s','%s') '''   %(sno,sname,scity))

    print("Rec is inserted ")
    conn.commit()
    cur.close()
    conn.close()
    
else:
    print("Connection is Fail")



