"""Create a program that reads data from a file specified by the user. 
   Handle exceptions when the file does not exist, cannot be opened, 
   or the user provides an invalid file name.
"""

try :
    file_name = input("Enter file name : ")
    with open(file_name, "r") as file:
        print(file.read)
except FileNotFoundError as e :
    print("Error : File doesn't exist")
except IOError :
    print("Error : Invalid input type")
