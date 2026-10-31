# from mypackage.signup.signup import dict 
def search(dict):
    print("welcome student data search")
    email=input("enter your email : ")

    if email in dict:
       print(dict)

    else:
        print("not found ")