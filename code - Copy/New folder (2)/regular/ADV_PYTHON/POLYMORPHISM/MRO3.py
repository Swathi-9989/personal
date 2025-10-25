#mro( ) -> list
import time

class A:
    pass

class B:
    pass

class C(A,B):
    pass

#calling
lst=C.mro()
for i in lst:
    time.sleep(.2)
    print(i)
