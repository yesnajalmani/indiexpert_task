def signup():
    dic={}  
    # while True:
    #         dic["name"]=input("enter your name : ")
    #         if len(dic["name"])>=3 and dic["name"].isalpha():
    #             break
    #         else:
    #             print("invalid name")

    # while True:
    #         dic["id"]=input("enter your id : ")
    #         if len(dic["id"])<5 and dic["id"].isdigit():
    #             break
    #         else:
    #             print("invalid id")
    
    # while True:
    #         dic["age"]=input("enter your age  :")
    #         if len(dic["age"])>0 and dic["age"].isdigit():
    #             break        
    #         else:
    #             print("not exist age")

    # qul=int(input("enter how many qualification :-"))
    # dic["qualification"]=[]
    # for q in range(qul):
    #     q=input("enter qualification :-") 
    #     dic["qualification"].append(q)
    #     print(dic["qualification"])

    while True:
        dic["email"]=input("enter your email : ")
        if "@"  in dic["email"] and  dic["email"].endswith(".com"):
            
            break
        else:
            print("invalid amail") 

    while True:
            dic["password"]=input("enter your password : ")
            if len(dic["password"])>=4 and dic["password"].isdigit():
                break
            else:
                print("incorrect password , please try again") 
         
    print("----signup successfully---- ")
    return dic
  



def login(dic):
    email=input("enter your email : ")
    password=input("enter your password : ") 
    if email== dic["email"] and password==dic["password"]:
        print("-----login succesfull-----")
    else:
        print("invalid email or password:")


def menu():
    dic = None
    while True:
            print("======== menu =========")
            print("1. signup")
            print("2. login")
            print("3. exit")
            choice=input("enter your choice :")
            if choice=="1":
                dic = signup()
            elif choice=="2":
                if dic is None:
                    print("please sign up first")
                else:
                    login(dic)
            elif choice=="3":
                print("exit")  
                break
            else:
                print("Invalid choice!")  

menu()

        
