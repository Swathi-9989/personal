
'''
  os.path.exists(path) -> bool
  os.path.isfile(path) -> bool
  os.path.isdir(path) -> bool
'''

import os.path

path="h:\\adv_super\\html"

if os.path.exists(path):
    print("Path is Existed ")
else:
    print("Specified path is not Existed ")
