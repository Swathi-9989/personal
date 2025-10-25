import cx_Oracle

conn=cx_Oracle.connect
("scott","Tiger9","localhost:1521/orcl")

if conn!=None:
    print("Connection is Est")

    cur=conn.cursor()
    print("Cursor object is created ")

    cur.execute('''INSERT INTO MASTINFO
                                VALUES(10,'SAI','KMM') ''')

    print("Rec is inserted ")
    conn.commit()
    cur.close()
    conn.close()
    
else:
    print("Connection is Fail")



