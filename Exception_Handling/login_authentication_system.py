"""Design a login system that validates username and password. 
   Handle scenarios such as incorrect credentials, empty input fields, 
   and account lock after multiple failed attempts.
"""

correct_username = "admin"
correct_password = "9876"

try :
    username = input("Enter username : ")
    password = input("Enter Password : ")
    if (username != correct_username) and (password != correct_password) :
        raise Exception("Please Enter valid login credentials ")
    print("Login Successful")

except Exception :
    print("Invalid Login Credentials")
