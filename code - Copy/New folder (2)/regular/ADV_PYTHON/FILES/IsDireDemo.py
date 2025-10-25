
'''
  os.path.exists(path) -> bool
  os.path.isfile(path) -> bool
  os.path.isdir(path) -> bool
'''

import os.path

path="h:\\adv_super\\html"

if os.path.exists(path):
    print("Specified path is Existed ")
    if os.path.isdir(path):
        print("Specified path is directory")
else:
    print("Specified path is not existed ")
