"""
Problem Statement
Total order amount:
≥ 5000 → 20% discount
≥ 3000 → 10%
≥ 1000 → 5%
Else → No discount

Print final payable amount.
Input:
amount
Output:
payable_amount

Sample Input:
3200
Sample Output:
2880

Hint:
Apply only one highest applicable discount.

"""

def total_price(amount):
    if amount >= 5000:
        return int(amount - amount * 0.20)
    elif amount >= 3000:
        return int(amount - amount * 0.10)
    elif amount >= 1000:
        return int(amount - amount * 0.05)
    else:
        return amount

amount = int(input())
result = total_price(amount)
print(result)