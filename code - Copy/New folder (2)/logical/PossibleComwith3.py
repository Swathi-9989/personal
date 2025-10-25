import time

a=int(input("Enter a number : "))
b=int(input("Enter b number : "))
c=int(input("Enter c number : "))
d=[]

d.append(a)
d.append(b)
d.append(c)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if (i!=j and j!=k and k!=i):
                time.sleep(.2)
                print(d[i],d[j],d[k])
