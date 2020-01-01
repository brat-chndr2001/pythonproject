#python_project
print("Registration/Login")
a=input()
if a=="registration":
    file=open("registrationuser.txt","a")
    file.write("\n")
    file.write(input("Username: "))
    file.write("\n")
    file.write(input("Password: "))
    file.write("\n")
    file.write("___________")
    file.write("\n")
    print("Successfully Registered")
elif a=="login":
    b=input("Username: ")
    c=input("Password: ")
    with open('registrationuser.txt') as file:
      if a and b in file.read():
          print("Successfully Logged In")
      else:
          print("Incorrect Username Or Password")