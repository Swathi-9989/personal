'''we can define the function inside another function
called closure . Adv is code reusablity '''
import time

def myFun():
    def stars():
        for i in range(1,11):
            time.sleep(.2)
            print("*",end=' ')

    stars()
    print("\n welcome")
    stars()
    print("\n To my world")
    stars()

#calling
myFun()
