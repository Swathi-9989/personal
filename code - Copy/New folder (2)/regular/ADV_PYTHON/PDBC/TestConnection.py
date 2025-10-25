
import cx_Oracle

conn=cx_Oracle.connect("scott","Tiger9","localhost:1521/Orcl")

if conn!=None:
    print("Connection is Est")
else:
    print("Connection is Fail ")

    
