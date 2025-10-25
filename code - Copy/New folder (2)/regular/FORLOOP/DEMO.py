
'''
Syn:
for <variable> in  <iterable>:
.... stmt(s)

iterable : is the collection or sequence with countable
no.of.objects from where we can read one by one
object

Eg:  list, tuple , set, str, dict, range, dict_keys ,
        dict_values, dict_items,map, filter, zip,
        file, cursor.....        
'''
import time

lst=[30,12.12,"Ramesh","Munny",123]
print("list : ",lst)

for i in lst:
    time.sleep(.2)
    print(i)
print("===========================")

t=(10,12.12,"Ramesh",None,"Manasa")
print("tuple : ",t)

for i in t:
    time.sleep(.2)
    print(i)
print("===========================")

s={40,50,60,12.12,"Ramesh","Munny"}
print("set : ",s)
for i in s:
    time.sleep(.2)
    print(i)
print("==============================")

st="welcome" #str is collection of char seq
print("string : ",st)

for i in st:
    time.sleep(.2)
    print(i)
print("===============================")

stu={"sno":101,"sname":"ramesh","sage":23}
print("stu : ",stu)

for i in stu:
    time.sleep(.2)
    print(i)

















    



    





















