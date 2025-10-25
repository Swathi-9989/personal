Based on the storage of the data
programs are classified into 2 types
1.Non Persistency Prgs.

2.Peristency Prgs.
     - Can Be Done by using
           > Files
           > Databases

open( )
   Syn:   open(filename,filemode) -> File class object

   File modes
   
   "w" : write mode
             - It will open the file and allows us to write
               the data into the file.
             - If the specified file is already existed then
               it will overwrite old with new data.

    "a" : append mode
           - It will open the file and allows us to write the
           data into the file.If the specified file is already
           Existed then it will add new data to its previous

    "r":  read mode | it is the default mode
                      f=open("data1.txt","r") or
                      f=open("data1.txt")
                      
             > If the specified file is not existed then it will
             raise an Error "FileNotFoundError'''

     "x": Exclusive mode
          - It will open the file and allow us to write the data
          into the file, iff the specified file is not existed.
          If the specified file is already Existed then it will
          raise an Error "FileExistsError"

      "w+" : Write and read
      "a+":   append and read 

name
mode
closed

writable()
readable()
close( )

For Writing the data
1.write(data)
2.writelines(iterable)

For Reading
1.read( ) -> str
2.read(bytes) -> str
3.readline( ) -> str
4.readlines( ) -> list of strs 
























        


            

            









                      

           
           






             
             





             


           
