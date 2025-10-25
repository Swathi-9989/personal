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
print("sno is : {n} and sname is : {na}".
      format(n=sno,na=sname))

print("sno is : {n} and sname is : {na} {na} is super".
      format(na=sname,n=sno))




       

















