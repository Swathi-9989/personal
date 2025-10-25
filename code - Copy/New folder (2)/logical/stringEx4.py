''' a=Roja
    b=RamaNI"

    Output: RRoajmaaNI
'''

#App-1
a="Roja"
b="RamaNI"
c=""

i,j=0,0
while i<len(a) or j<len(b):
    if i<len(a):
        c=c+a[i]
        i=i+1

    if j<len(b):
        c=c+b[j]
        j=j+1

print("Res : ",c)







