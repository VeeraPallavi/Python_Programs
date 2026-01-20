"""
Problem Statement
Fare rules:
Distance * ₹2/km
Senior citizen → 30% discount
Child (<12) → 50% discount
Input
distance
age
Output
fare

Sample Input
200
65
Sample Output
280

Hint:
Calculate base fare first, then apply age-based rule.
"""
def total_amount(distance, age):
    amount = distance * 2
    if age >= 60:
        return int(amount - amount * 0.30)
    elif age < 12:
        return int(amount - amount * 0.50)
    else:
        return amount

distance = int(input())
age = int(input())
print(total_amount(distance, age))