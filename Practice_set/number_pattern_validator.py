"""
Check if digits of a number are strictly increasing left to right.
Input
number
Output
YES / NO

Sample Input
13579
Sample Output
YES

Hint:
Compare adjacent digits.

"""
def is_increasing(number):
    num = str(number)
    n = len(num)

    for i in range(n-1):
        if num[i] > num[i+1]:
            return False
    return True

number = int(input())
result = is_increasing(number)
if result:
    print("YES")
else:
    print("NO")