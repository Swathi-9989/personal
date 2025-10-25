#sorted(iterable,key=None,reverse=False) -> list 
t=(50,60,40,10,20,30)
print("tuple : ",t)
lst=sorted(t)   #to convert to list to tuple tuple(iterable)
t=tuple(lst)
print("Res : ",t)
print("=========================")

s={40,50,30,10,20,70}
print("set : ",s)
lst=sorted(s)  #conver list to set
print("Res : ",lst)
print("=========================")

st="bcdefagh"
print("String : ",st)
lst=sorted(st)  #convert iterable to str  #s.join(iterable) -> str
st="".join(lst)
print("Res : ",st)
print("=========================")































