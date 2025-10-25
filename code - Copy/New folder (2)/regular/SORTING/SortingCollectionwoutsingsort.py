#Code for ASC 
import time

a=[10,40,30,20,50]
print("Before sort : ",a)

for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp

print("After sorting : ",a)
    
