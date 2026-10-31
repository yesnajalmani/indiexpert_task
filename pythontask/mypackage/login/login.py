
# from mypackage.signup.signup import dict
def login(dict):
    print("-------login------")
    email=input("enter your email : ")
    password=input("enter your password : ")

    if email in dict and dict[email]["password"] in password:
        print("login successfully")
    else:
        print("try again")

import datetime
now=datetime.datetime.now().time()
print(now)