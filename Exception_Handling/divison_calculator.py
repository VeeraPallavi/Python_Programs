"""Design a program that takes two numbers from the user and performs division. 
   Handle situations where the user enters zero as the divisor or provides invalid input.
"""


num = int(input("Enter numerator: "))
den = int(input("Enter Denominator : "))

try :
    result = num / den
    print(result)

except ZeroDivisionError as e :
    print(e)
except ValueError as e1 :
    print(e1)