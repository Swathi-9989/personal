import time

stu={
            "sno": 101,
            "sname":"Roja",
            "sage":23,
            "Address": { "Hno":"1-2-3",
                                     "City":"Hyd",
                                     "Pin":"500090"
                                  },
            "Marks":[50,60,70,80]            
        }

for k,d in stu.items():
    time.sleep(.2)
    if isinstance(d,dict):
        print(k)
        for k1,d1 in d.items():
            time.sleep(.2)
            print("    ",k1," >>> ",d1)

    elif isinstance(d,list):
        print(k)
        print("   ",d)

    else:
        print(k," >>> ",d)



