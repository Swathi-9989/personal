#Swaping the nth pos elements or kth pos elements 

#       0    1   2     3   4    5
lst=[10,20,30,40,50,60]
#       -6  -5  -4   -3  -2  -1
print("list : ",lst)

n=int(input("nth pos : "))
lst[n-1],lst[-n]=lst[-n],lst[n-1]
print("Res : ",lst)

