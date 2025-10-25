#L.extend(iterable)

a=[1,2,3]
b=[4,5,6]
print("list a : ",a)
print("list b : ",b)

c=a+b   #list + list -> list 
print("Res : ",c)

a.extend(b)  #[1,2,3,4,5,6]
print("Res : ",a)
