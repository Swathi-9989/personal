
a=int(input("Enter a: "))
b=int(input("Enter b : "))
c=int(input("Enter c: "))
d=int(input("Enter d: "))

if a>b and a>c and a>d:
    print("a is big")
elif  b>c and b>d:
    print("b is big")
elif  c>d:
    print("c is big")
else:
    print("d is big")
