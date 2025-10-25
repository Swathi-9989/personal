#D.keys( ) -> keys | iterable
#D-Dict | k-key | d-value
#D.values( ) -> dict_values | iterable
#D.items( ) -> dict_items | iterable
#dict_items is list of tuples
#D.update({k:d})
#D.copy( ) -> shallow copy of dict

a={"a":"anu","b":"balu"}
print("dict a : ",a)

b=a.copy()
print("dict b : ",b)

a.update({"c":"cnu"})
print("After modification ")
print("dict a : ",a)
print("dict b : ",b)





