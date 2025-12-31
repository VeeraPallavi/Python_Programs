"""Create a program that checks eligibility based on age. 
   Handle exceptions when the user enters a negative value, 
   a string instead of a number, or an unrealistic age.
"""
try :
    age = int(input("Enter age : "))
    if age < 0 :
        raise ValueError("Negative values not allowed ")
    if age > 100 :
        raise Exception ("Enter valid age : ")
    print(f"Age : {age}")
except ValueError as e:
    print(e)
except Exception :
    print("Enter valid Age ")