#D.keys( ) -> keys | iterable
#D-Dict | k-key | d-value

stu={"sno":101,"sname":"ramesh","sage":23}
print("stu : ",stu)

keys=stu.keys()
print("keys : ",keys)

import time
for k in keys:
    time.sleep(.2)
    print(k)
