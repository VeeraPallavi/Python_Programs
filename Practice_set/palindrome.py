"""
Number Mirror Validator
Problem Statement
Reverse a number and check if original equals reversed.
Input
number
Output
PALINDROME / NOT PALINDROME

Sample Input
1221
Sample Output
PALINDROME

Hint:
Build reverse using arithmetic.

"""

def is_palindrome(number):
    original_number = number
    rev =0
    while(number != 0):
        rem = number % 10
        rev = rev * 10 + rem
        number = number // 10
    if original_number == rev:
        print("PALINDROME")
    else:
        print("NOT PALINDROME")

number = int(input())
is_palindrome(number)