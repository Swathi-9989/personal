'''Note: Default thread in python is main thread.
Main thread is automatically executed thread.

Q:    How to get the object of current working thread ?
Ans:  By using current_thread( ) -> Thread object
              from threading module

> Default thread in python is main thread.
> Main thread is not always current Thread
'''

import threading
ct=threading.current_thread()
print("Thread Name : ",ct.name)
