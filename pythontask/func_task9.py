def student():
    
    name=input("enter your name : ")
    id= int(input("Enter your id: "))
    age=int(input("enter your age : "))
    qualification= input("Enter your qualification: ")
    address=input("enter your address : ")
    email=input("Enter your email: ")

    dic={"name":name,
         "id": id,
         "age":age,
         "qualification":qualification,
        "address":address ,
        "email":email
}

    print(dic)
student()