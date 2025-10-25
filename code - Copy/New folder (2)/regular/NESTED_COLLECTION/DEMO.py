'''Nested Collection is process of defining the collection
or collections inside another collection '''

lst=[10,12.12,
        [11,22,33],
        (1.1,2.2,3.3),
        {"aaa","bbb","ccc"},
        {"sno":101,"sname":"ramesh","sage":23}
      ]

print("Inner list : ",lst[2])
print("2nd item : ",lst[2][1])
print("Inner Set : ",lst[4])
print("Inner Dict : ",lst[5])
print("sname is : ",lst[5]['sname'] )
print("sname is : ",lst[5].get('sname'))






