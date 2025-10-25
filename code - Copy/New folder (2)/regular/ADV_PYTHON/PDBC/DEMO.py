Steps for PDBC
===============
1.import cx_Oracle module and if required
   any other module.

   import cx_Oracle
   import time

2.Establish the connection with Oracle Database
by using connect( ) function from cx_Oracle

connect(str,str,str) -> connection class
str : username of Database Eg: In Oracle UN : scott
str : password of database user Eg: In Oracle : Tiger9
str : DB Information
                location : portnumber / serviceid

location
   - place where database is installed.

   - if the database is installed in the same system
       then we have to rep by using "localhost"

   - if the database is avaiable in the different machine
     then we have to write  "IPAddres  of the Machine "

portnumber : Every database will have unique and
fixed port number . Default port number for oracle
database is 1521

Service ID : Every Database will also have unique
service id . Default Service id of oracle database
is : Orcl

To Know the Service ID of Oracle Database
SQL>Select * from global_name;


import cx_Oracle

conn=cx_Oracle.connect
("scott","Tiger9","localhost:1521/Orcl")

if conn!=None:
    print("Connection is Est")
else:
    print("Connection is Fail ")

Step-3: Create cursor class object for sending the
queries to the database by using cursor( ) mtd from
connection class.

cursor( ) -> cursor class object

cur=conn.cursor()
print("cursor object is created ")

Example:
   
import cx_Oracle

conn=cx_Oracle.connect(
   "scott","Tiger9","localhost:1521/orcl")

if conn!=None:
    print("Connection is Est")
    
    cur=conn.cursor()
    print("Cursor object is created ")
    
else:
    print("Connection is Fail")

Step-4: Use the cursor class object for sending
queries to execute at Oracle Database by using
execute( ) mtd from cursor class

execute(str)
   |str rep any oracle query
        create, insert, update, delete, select...

Note-1: After  insert,update, delete command then
we have to call commit( ) from connection class otherwise
those changes are not effected to the database.

Note-2: If u want cancel the last transaction then we
have to call rollback( ) from connection class.

Note-3: AFter executing any select statement then
result of the select statement will be stored in the
same cursor class object.

> If u want read the records from the cursor class object
then we have to call the following methods  from cursor
class

fetchone( ) -> tuple
fetchmany( ) -> list of tuples
fetchall( ) -> list of tuples

Note: After All DB Operations then we
have to close the cursor and connection
class objects

cur.close()
con.close()
































        







































     
    



   





                



