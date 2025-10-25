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
print("sno is : {}".format(sno))

sname="Ramesh"
print("sname is : {}".format(sname))

print("sno is : {} and sname is : {}".
      format(sno,sname))

print("sno is : {} and sname is : {}".
      format(sname,sno))












