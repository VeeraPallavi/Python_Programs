"""Build a system that accepts student marks. 
   Handle exceptions when marks are entered outside the valid range (0–100) or 
   when the input is not a number.
"""

try :
    marks = int(input("Enter marks : "))
     
    if marks < 0 or marks > 100 :
        raise Exception ("Please neter Valid marks ")
    print(f"Marks : {marks}")
except ValueError as e :
    print(e)
except Exception :
    print("Please Enter valid marks")