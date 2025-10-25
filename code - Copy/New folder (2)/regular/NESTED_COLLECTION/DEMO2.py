import time
lst=[
        [11,22,33],
        (1.1,2.2,3.3),
        {"aaa","bbb","ccc"},
        {"sno":101,"sname":"ramesh","sage":23}
      ]

for i in lst:
    time.sleep(1)
    print("Type is : ",type(i))
    print("Data is : ",i)
    if isinstance(i,dict):
        for k,d in i.items():
            time.sleep(.2)
            print(k," >> ",d)
    else:
        for j in i:
            time.sleep(.2)
            print(j)
    print("========================")




    
    




