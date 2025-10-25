'''
   Constructor overloading
       >> Process of defining more the one constructor
       for different purpose in other prg.Language.       
'''
class Test:
    def __init__(self):
        print("Const with 0-args")

    def __init__(self,x):
        print("Const with 1-args",x)

#calling
t=Test(123)

