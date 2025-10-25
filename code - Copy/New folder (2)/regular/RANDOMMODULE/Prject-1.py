'''choice(seq) -> item '''

import time,random

lst=["java","python","oracle","ds"]
print("list : ",lst)

for i in range(1,11):
    sys=random.choice(lst)
    guess=input("Guess the course ? : ")

    if guess==sys:
        time.sleep(2)
        print("Congrats ...!!! u won course ",guess," Free ")
        break
        
