#    0    1    2    3   4    5
t=(10,20,30,40,50,60)
print("tuple : ",t)

pos=int(input("Enter pos : ")) #2

if pos>=0 and pos<len(t):
    new=int(input("Enter an item :"))    #int
    f=t[0:pos:1]
    s=t[pos: :1]
    #t=f+ (new,) +s      #tuple(iterable)
    t=f+tuple([new])+s
    print("After Insert : ",t)
else:
    print("Sorry invalid index")
