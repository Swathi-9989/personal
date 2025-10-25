
import random
import os

sys=random.randint(111111,999999)
print("U R OTP : ",sys)

user=int(input("Please U R OTP : "))

if user==sys:
    os.system('notepad')
else:
    print("Sorry Dear Invalid OTP ")


