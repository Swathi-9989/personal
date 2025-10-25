#ways to define the tuple collection
a=()
print("tuple : ",a)
print("=========")

b=(10,12.12,"Ramesh",10,None)
print("tuple : ",b)
print("=========")

c=(10,)
print("type is : ",type(c))
print("tuple  : ",c)
print("=========")

d=10,12.12,"Ramesh"   #packing | tuple
print("type is : ",type(d))
print("tuple : ",d)
print("=========")

#tuple( ) -> tuple
e=tuple( )
print("type is : ",type(e))
print("tuple : ",e)
print("=========")

#tuple(iterable) -> tuple
#typecasting function Converting other collections to
#tuple collection.

lst=[10,20,30,40,50,60]
print("list : ",lst)
f=tuple(lst)
print("tuple : ",f)
print("=========")

s={12,23,45,56,78}
print("set : ",s)
g=tuple(s)
print("tuple : ",g)
print("==============")

stu={"sno":101,"sname":"ramesh","sage":23}
print("stu : ",stu)
h=tuple(stu)
print("tuple : ",h)
print("=========")

st="welcome" #string is collection of char seq
print("str : ",st)
i=tuple(st)
print("tuple : ",i)



















