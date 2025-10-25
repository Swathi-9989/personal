
'''
  os.path.exists(path) -> bool
  os.path.isfile(path) -> bool
  os.path.isdir(path) -> bool
'''
import time
import os.path

path="h:\\adv_super\\html\\images.html"

if os.path.exists(path):
    print("Specified path is Existed ")
    if os.path.isfile(path):
        print("Specified path is File ")

        with open(path) as f:   #default mode is read
            data=f.read()
            for i in data:
                time.sleep(.02)
                print(i,end='')            
            
else:
    print("Specified path is not Existed ")











