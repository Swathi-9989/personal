#    0    1    2    3   4    5
t=(10,20,30,40,50,60)
print("tuple : ",t)

pos=int(input("Enter pos : ")) #2

if pos>=0 and pos<len(t):
    f=t[0:pos:1]
    s=t[pos+1: :1]
    t=f+s
    print("Result is : ",t)
else:
    print("Invalid index ")
    
