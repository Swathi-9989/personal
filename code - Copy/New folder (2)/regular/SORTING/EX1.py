#L.sort(key=None,reverse=False)
lst=[40,50,10,20,30,70]
print("list : ",lst)

lst.sort()
print("ASC Sort : ",lst)

lst.sort(reverse=True)
print("DEC Sort : ",lst)
print("========================")

#Note: set | str | tuple | dict  not supported for sort
#there is no sort method in the above collection.
#But can sort any collection by using sorted( ) function
#sorted(iterable,key=None,reverse=False) -> list 


t=(50,60,40,10,20,30)
print("tuple : ",t)
#t.sort() AttributeError
print("=========================")

s={40,50,30,10,20,70}
print("set : ",s)
#s.sort() AttributeError
print("=========================")

st="bcdefagh"
print("String : ",st)
#st.sort() AttributeError
print("=========================")

stu={"c":"cnu","a":"anu","b":"balu","d":"dhanu"}
print("stu : ",stu)
#stu.sort() AttributeError






























