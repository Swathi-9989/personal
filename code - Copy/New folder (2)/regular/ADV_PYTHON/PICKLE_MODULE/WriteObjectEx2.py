
import mymodule
import pickle

with open("myemp2.txt","wb") as f:
    
    while True:
        e=mymodule.Employee()
        pickle.dump(e,f)
        opt=input("Do u want another rec Y|N ? : ")
        print("------------------------------------------------")
        if opt in 'Nn':
            break
