#set doesn't support
#indexing
#slicing
#unpacking using slicing
#It will support unpacking and for
s={10,"Ramesh","Hyd"}
print("set : ",s)

a,b,c=s #unpacking
print(a,b,c,sep=' ... ')
print("=================")

a={10,12.12,"Ramesh",23,"Sudha"}
print("set a : ",a)
import time
for i in a:
    time.sleep(.2)
    print(i)







