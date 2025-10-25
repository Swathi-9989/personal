import mymodule
import pickle

with open("myemp1.txt","wb") as f:
    e=mymodule.Employee()
    pickle.dump(e,f)

print("Object is Saved ")
    
