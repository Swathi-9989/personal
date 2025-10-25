#bool type casting using bool(x) -> bool

#int -> bool
x=-123
y=bool(x)
print(type(x)," >> ",type(y))
print(x, " >>> ",y)
print("==================")

#float -> bool
x=0.0
y=bool(x)
print(type(x)," >> ",type(y))
print(x, " >>> ",y)
print("==================")

#str -> bool
x="1"
x="0"
x="0.0"
x="False"
x=" "
x=""
y=bool(x)
print(type(x)," >> ",type(y))
print(x, " >>> ",y)
print("==================")

#complex -> bool
x=10+20j
x=0+20j
x=10+0j
x=0+0j
y=bool(x)
print(type(x)," >> ",type(y))
print(x, " >>> ",y)
print("==================")















