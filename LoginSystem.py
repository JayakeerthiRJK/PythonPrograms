#Admin username and password
username = "admin"
password = 1234

print("ADMIN LOGIN")


#Getting input
admin_username = input("Enter the UserName: ")
admin_password = int(input("Enter the Password: "))

#if condition to check the username and password
if admin_username == username and admin_password == password:
    print("Login Successfull!")
elif admin_username != username and admin_password != password:
    print("Wrong Username And Password")
elif admin_username != username:
    print("Wrong Username!")
elif admin_password != password:
    print("Wrong Password!")

