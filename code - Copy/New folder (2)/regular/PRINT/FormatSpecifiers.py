''' Working with format specifiers
      Format specifiers are used to specify what types
      values tobe formatted during the output.

      datatype     Format specifiers
          int             %d
          float         %f
          str             %s

   Syn: print("format specifier"      %variable)
   Syn: print("format specifiers"    %(variables) )          
'''

sno=101    #int
print("sno is : %d" %sno)
sname="Sai"   #str
print("sname is : %s" %sname)
print("sno is : %d and sname is : %s" %(sno,sname) )
print("=========================================")

savg=99.99
print("savg is : %f" %savg)
print("savg is : %.2f" %savg)
















