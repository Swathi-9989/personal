''' Accept un and pw and ensure
username is sssit or not and
password is kphb or not
if not raise the MyLoginException [UDE]  '''

class MyLoginException(Exception):
    def __init__(self,msg):
        self.msg=msg

#main_logic
un=input("Enter username : ")
pw=input("Enter password : ")

if un=="sssit" and pw=="kphb":
    print("Valid user ")
else:
    try:
        raise MyLoginException('Invalid un or pw..')
    except MyLoginException as me:
        print("Sorry unable to continue....")
        print("Reason is : ",me)





