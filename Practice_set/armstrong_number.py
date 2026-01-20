import math
"""
Problem Statement
Check if a number equals sum of cubes of its digits.
Input
number
Output
YES / NO

Sample Input
153
Sample Output
YES

Hint:
Extract digits using modulo and division.

"""

def is_armstrong(number):
    sum =0
    while(number != 0):
        rem = number % 10
        sum = sum + math.pow(rem, 3)
        number = number // 10
    return sum
number = int(input())
result = is_armstrong(number)
if number == result:
    print("YES")
else:
    print("NO")