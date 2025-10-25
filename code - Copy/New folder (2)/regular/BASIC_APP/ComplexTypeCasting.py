
#complex typecasting
#by using complex(x) -> complex
#x-rep real part | where imag always remains 0

#by using complex(x,y) -> complex
#x-rep real part  | where y rep image part.
#Here string with other combinations are not supported

x=10
y=complex(x)
print("Result is : ",y)

x=1.23
y=complex(x)
print("Result is : ",y)

x=True
y=complex(x)
print("Result is : ",y)

x="123"
y=complex(x)
print("Result is : ",y)




