"""Develop a banking system where users can withdraw money from their account.
    Handle cases such as insufficient balance, negative withdrawal amount, 
    or invalid account number.
"""

balance = 5000
try : 
    amount = int(input("Enter amount to withdraw: "))
    if amount <= 0:
        raise ValueError("Invalid amount")
    if amount > balance :
        raise Exception("Insufficient Balance ")
    balance -= amount
    print(f"Withdrawl Successful . Remaining Balance :{balance}")
except ValueError :
    print("Please enter positive amount only ")

except Exception :
    print("Insufficient Balance ")
