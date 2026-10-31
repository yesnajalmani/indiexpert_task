def course():
    print("available course : ")
    print("1. python")
    print("2. c++")
    print("3. java script")

    choice= int(input("enter your choice: "))

    if choice==1:
      print("python")
    elif choice==2:
      print("c++")
    elif  choice==3:
      print("java script")
    else:  
      print("not course available")
