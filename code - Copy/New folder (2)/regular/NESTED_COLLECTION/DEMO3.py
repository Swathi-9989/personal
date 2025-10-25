import time
t=(
        [11,22,33],
        (1.1,2.2,3.3),
        {"aaa","bbb","ccc"},
        {"sno":101,"sname":"ramesh","sage":23}
     )

for i in t:
    if isinstance(i,tuple):
        print("Data is : ",i)
        for j in i:
            time.sleep(.2)
            print(j)
        print("=============")

    elif isinstance(i,dict):
        print("Data is : ",i)
        for k,d in i.items():
            time.sleep(.2)
            print(k," >>> ",d)
        


            
            
            
