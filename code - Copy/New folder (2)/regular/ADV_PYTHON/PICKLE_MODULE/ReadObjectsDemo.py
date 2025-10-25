import time
import mymodule
import pickle

with open("myemp2.txt","rb") as f:

    while True:
        time.sleep(1)
        try:
            e=pickle.load(f)
        except EOFError:
            break
        else:
            e.getEmployee()
        print("------------------")
    
