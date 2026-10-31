dict={}
def signup(dict):

    print("========== signup ===========")
    name=input("enter name :-")
    student_id=input("enter student's id :-")
    age=int(input("enter age :-"))
    email=input("enter email :-")
    password=input("enter password :-")
    n=int(input("enter how many qualification :-"))

    for i in range(n):
        qul=input("enter qualification :-")

    if email in dict:
        print("already registered...")

    print("========= signup successfully =========")

    import datetime
    now=datetime.datetime.now()
    print(now)

    dict[email]={
        "name":name,
        "student_id":student_id,
        "age":age,
        "qul":qul,
        "email":email,
        "password":password
    }

print(dict)    

def validation(): 
    if "@"  and ".com" in "email":
         print("valid email")
    else:
        print("invalid email")

def p():
    if "password"<="5":
        print("correct password")
    else:
         print("incorrect password")
