"""
Problem Statement
Given a password string:
Must contain at least 1 digit
Must contain at least 1 uppercase
Length ≥ 8
Print STRONG or WEAK.

Input:
password

Output:
STRONG

Sample Input:
Pass1234

Sample Output:
STRONG

Hint:
Loop through characters and count conditions manually.

"""
def password_evaluator(password):
    upper = False
    digit = False
    if len(password) < 8:
        print("WEAK")
        return
    for ch in password:
        if ch.isupper():
            upper = True
        if ch.isdigit():
            digit = True
    if upper and digit :
        print("STRONG")
    else:
        print("WEAK")

password = input()
password_evaluator(password)