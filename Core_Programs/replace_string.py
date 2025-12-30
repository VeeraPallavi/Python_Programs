user_name=input("Enter Name: ")

if(len(user_name)<3):
    print("UserName must be minimum 3 characers")
else:
    print(f"Hello {user_name}, How are you?")