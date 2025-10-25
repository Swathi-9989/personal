#       0    1    2   3    4   5   6
lst=[30,40,50,20,10,60,70]
print("list : ",lst)

pos=int(input("Enter pos : "))
try:
    item=lst[pos]
except IndexError:
    print("IE : Sorry Invalid Index ")
else:
    print("Item @ given index : ",item)
