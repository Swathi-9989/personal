''' a=Roja
    b=Rama"

    Output: RRoajmaa
'''

#App-1
a="Roja"
b="Rama"
c=""
for i in range(len(a)):
    c=c+a[i]+b[i]
print("Res : ",c)

#App-2
a="Roja"
b="Rama"
c=""
i,j=0,0
while i<len(a) or j<len(b):
    c=c+a[i]+b[j]
    i=i+1
    j=j+1
print("Res : ",c)








    





