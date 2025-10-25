#D.keys( ) -> keys | iterable
#D-Dict | k-key | d-value
#D.values( ) -> dict_values | iterable

stu={"sno":101,"sname":"ramesh","sage":23}
print("stu : ",stu)

values=stu.values()
print("values : ",values)

import time

for v in values:
    time.sleep(.2)
    print(v)
