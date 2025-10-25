
#complex typecasting
#by using complex(x) -> complex
#x-rep real part | where imag always remains 0

#by using complex(x,y) -> complex
#x-rep real part  | where y rep image part.
#Here string with other combinations are not supported

x=10
y=12.12
z=complex(x,y)   #10+12.12j
print("Result is : ",z)
print("================")

x=True
y=False
z=complex(x,y)
print("Result is : ",z)

x="123"
y=True
#z=complex(x,y)
z=complex(y,x)








