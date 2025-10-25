#mro( ) -> list

import time

class A:
    pass

class B(A):
    pass

#calling
lst=B.mro()
for i in lst:
    time.sleep(.2)
    print(i)
