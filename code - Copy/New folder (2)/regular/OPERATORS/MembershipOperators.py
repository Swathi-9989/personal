''' Membership Operators are used ensure
the existency of the specified object in the collection
list , tuple, set, str, dict, .... 

Membership Opertors are classified into 2 tyes
1.in : Returns True iff the specified object is
                 Existed in the collection
                      Syn:   object in iterable      
    
2.not in : Returns True iff the specified object
             is not existed in the collection
                     Syn: object not in iterable '''

print("w" in "welcome") #True
#print(w in "welcome") #NameError

lst=[40,50,30,10,560]
print("50 in lst ? : ",50 in lst)
print("90 not in lst ? : ",90 not in lst)

stu={"sno":101,"sname":"ramesh"}
print("stu : ",stu)
print("101 in stu ? : ",101 in stu)  #False
print("sname in stu ? : ","sname" in stu) #True
















