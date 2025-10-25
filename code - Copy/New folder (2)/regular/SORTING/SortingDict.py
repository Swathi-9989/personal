#sorted(iterable,key=None,reverse=False) -> list

stu={"c":"cnu","a":"anu","b":"balu","d":"dhanu"}
print("stu : ",stu)

sk=sorted(stu.keys()) #[a,b,c,d]
sv=sorted(stu.values()) #[anu,balu,cnu,dhanu]

z=zip(sk,sv)
#dict(iterable)
#here iterable is a dict or any other object same as dict

d=dict(z)
print("Stu : ",d)

