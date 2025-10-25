'''
Defining the thread by creating
the sub class of thread

1.Create class that should be the sub class of class
   thread

   class Cat(threading.Thread):
        pass

2.Whatever the logic u want execute as thread then
that logic must be define inside of run( ) of thread class.

3.run( ) method of thread class shouldn't call explicitly
rather we have to call start( ) of thread class.

'''
import threading
class Cat(threading.Thread):
    def run(self):
        for i in range(1,11):
            print("Cat ... ",i)

class Rat(threading.Thread):
    def run(self):
        for i in range(20,31):
            print("Rat >>> ",i)

#calling
c=Cat()
r=Rat()
c.start()
r.start()

















