import mypackage
student={}
def menu():
    while True:
        print("1.signup")
        print("2.login")
        print("3.profile")
        print("4.cousre")
        print("5.search")
        print("6.logout")

        choice =int(input("please enter the choice:"))

        if choice ==1:
            mypackage.signup(student)
        elif choice ==2:
           mypackage.login(student) 
        elif choice ==3:
            mypackage.profile(student)
        elif choice ==4:
            mypackage.course()
        elif choice ==5:
           mypackage.search(student)
        elif choice ==6:
            print("id is logout") 
        else:
            print("data is not found")       

if __name__=="__main__":
 menu()   

