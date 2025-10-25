import time

'''
s={
        [11,22,33],
        (1.1,2.2,3.3),
        {"aaa","bbb","ccc"},
        {"sno":101,"sname":"ramesh","sage":23}
     }
TypeError: unhashable type: 'list'

s={
        (1.1,2.2,3.3),
        {"aaa","bbb","ccc"},
        {"sno":101,"sname":"ramesh","sage":23}
     }
TypeError: unhashable type: 'set'

s={
        (1.1,2.2,3.3),
        {"sno":101,"sname":"ramesh","sage":23}
     }
TypeError: unhashable type: 'dict'
'''

s={
        (1.1,2.2,3.3),
        (111,222,333),
        ("aaa","bbb","ccc")
     }

import time

for i in s:
    time.sleep(.2)
    print(i)
    for j in i:
        time.sleep(.2)
        print(j)













