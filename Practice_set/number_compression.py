"""
Problem Statement
Given a number, count how many times it can be divided by 2 until it becomes odd.
Input
number
Output
count

Sample Input
40
Sample Output
3

Hint:
Use a loop and modulo check.

"""
def number_counter(number):
    count = 0
    while number % 2 == 0:
        count += 1
        number = number // 2
    return count

number = int(input())
print(number_counter(number))