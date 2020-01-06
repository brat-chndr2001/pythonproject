#python_project
print("What details you want to update in your profile")
print("Update username or password or both")
a=input()
if a=="username":
     file=open("updateprofile.txt","a")
     file.write("\n")
     file.write(input("New Username: "))
     file.write("\n")
     print("Username updated successfully")
elif a=="password":
     file=open("updateprofile.txt","a")
     file.write("\n")
     file.write(input("New Password: "))
     file.write("\n")
     print("Password updated successfully")
else:
     file=open("updateprofile.txt","a")
     file.write("\n")
     file.write(input("New Username: "))
     file.write("\n")
     file.write(input("New Password: "))
     file.write("\n")
     print("Username and Password updated successfully")
              



