''' Working with replacement fields
     >> Replacement fields are rep by using  { }
     >> Replacements fields are from C#.net
     >> while working with replacement fields
           we have to use format( ) from str class.

     >> Replacements fields are 2 types
              1.Automatic field numbering system
              2.Manual Field Specification
                      a.Index Based
                      b.Name Based

    Syn: print("replacement fields".format(variable(s))    
'''
sno=101
sname="Ramesh"

print("sno is : {0} and sname is : {1}".
      format(sno,sname))
       #             0         1
print("sno is : {1} and sname is : {0}".
      format(sname,sno))
      #                 0         1
sage=23
print("sno is : {2} sname is : {0} sage : {1}".
      format(sname,sage,sno))
       #              0         1         2

print("sno is : {2} sname is : {0} sage : {1}".
      format(sname,sage,sno))
       #              0         1         2
       
print("sno is : {1} sname is : {0}  {0} is super".
      format(sname,sno))
       







       

















