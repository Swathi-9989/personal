#D.keys( ) -> keys | iterable
#D-Dict | k-key | d-value
#D.values( ) -> dict_values | iterable
#D.items( ) -> dict_items | iterable
#dict_items is list of tuples

#D.update({k:d})
'''
1.For adding new item to the dict collection
2.For updating an existed item
3.For dict concatenation.
'''

stu={}

for i in range(1,4):
    k=input("Enter key : ")
    d=input("Enter value : ")
    stu.update({k:d})

print("stu : ",stu)















