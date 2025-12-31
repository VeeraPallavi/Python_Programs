"""
    ATM Transaction Validator

    Problem Statement : 

    An ATM processes N withdrawal requests sequentially.
    Each request has an amount. 
    Rules:
    Withdrawal amount must be a multiple of 100
    Account balance must never go negative
    For each transaction, print SUCCESS or FAILED

    Input
    InitialBalance
    N
    amount1
    amount2
    ...
    amountN

    Output  
    SUCCESS
    FAILED
    SUCCESS
    ...
    FinalBalance

"""

def transaction_validator(initial_balance, N):
    for _ in range(N):
        amount = int(input())
        if amount % 100 == 0 and initial_balance > 0 :
            print("SUCCESS")
            initial_balance -= amount
            if(initial_balance < 0):
                initial_balance = initial_balance + amount 

        else :
            print("FAILED")
        

    print(initial_balance)   

initial_balance = int(input())
N = int(input())
transaction_validator(initial_balance, N)