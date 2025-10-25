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

stu={"sno":101,"sname":"khanna"}
print("stu : ",stu)
stu.update({"sname":"chinni"})
print("stu : ",stu)
print("======================")

a={"a":"anu","b":"balu"}
b={"c":"cnu","d":"dhanu"}
#a+b
print("a : ",a)
print("b : ",b)

a.update(b)
print("dict concat : \n ",a)






















