username = "python"
password = "rules"
username_login = input("Enter username: ")
password_login = input("Enter password: ")
attempts = 5
while (username_login != username or password_login != password) and attempts >0:
    username_login = input("Enter username: ")
    password_login = input("Enter password: ")
    attempts = attempts -1
if username_login == username and password_login == password:
        print("Welcome")
if attempts == 0:
    print("Access Denied")

# Output
# Enter username: Ghazanfar
# Enter password: Abbas
# Enter username: python
# Enter password: rules
# Welcome
