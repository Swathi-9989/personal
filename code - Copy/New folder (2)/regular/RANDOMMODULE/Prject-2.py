
import sys
import random

for i in range(1,11):
    sys=random.randint(1,9)
    guess=int(input("Guess the no [1-9] : "))

    if guess<sys:
        print("Sorry guess is too low... ")
    elif guess>sys:
        print("Well guess is too high....")
    elif guess==sys:
        print("Great work Guess is correct ")
        break
