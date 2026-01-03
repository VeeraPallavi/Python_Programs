"""
Problem Statement
User gets 3 attempts to enter correct PIN.
Correct → ACCESS GRANTED
All wrong → LOCKED

Input
correct_pin
attempt1
attempt2
attempt3
Output
ACCESS GRANTED / LOCKED

Sample Input
4321
1111
2222
4321
Sample Output
ACCESS GRANTED

Hint:
Exit loop early on success.

"""

def door_lock(correct_pin):
    for _ in range(3):
        pin = int(input())
        if(correct_pin == pin):
            return True
    return False

correct_pin = int(input())
result = door_lock(correct_pin)
if result :
    print("ACCESS GRANTED")
else:
    print("LOCKED")