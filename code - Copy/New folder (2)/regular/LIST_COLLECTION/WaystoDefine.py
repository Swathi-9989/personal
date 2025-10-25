a=[]
print("type is : ",type(a))
print("data is : ",a)
print("===============")

b=[10,12.12,"Ramesh",None,10,"Sudha"]
print("type is : ",type(b))
print("data is : ",b)
print("=====================")

#list( ) -> list
c=list()
print("type is : ",type(c))
print("data is : ",c)
print("=====================")

#list(iterable) -> list
#typecasting for converting other collection to list
t=(10,12.12,"Ramesh")
print("tuple : ",t)
d=list(t)
print("data is : ",d)
print("========================")

s={10,20,30,12.12,"Ramesh","Suresh"}
print("set : ",s)
e=list(s)
print("data is : ",e)
print("========================")

st="welcome" #string is collection of char seq
print("str : ",st)
f=list(st)
print("data is : ",f)
print("=======================")

stu={"sno":101,"sname":"ramesh","sage":23}
print("dict : ",stu)
g=list(stu)
print("data is : ",g)
print("==================")

#range(stop) -> range object | iterable
#range(start,stop,step=1) -> range object | iterable

h=list( range(1,21) )
print("list : ",h)


















