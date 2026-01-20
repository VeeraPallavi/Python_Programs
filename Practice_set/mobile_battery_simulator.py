"""
Problem Statement
Battery starts at 100%. Each app drains fixed % per minute.
Stop when battery ≤ 0. Print minutes used.
Input:
drain_per_minute
Output:
minutes

Sample Input
7
Sample Output
15

Hint:
Use a loop until battery <= 0.

"""
def minutes_used(drain_per_minute):
    battery = 100
    minute =0
    while battery > 0:
        battery = battery - drain_per_minute
        minute += 1
    return minute

drain_per_minute = int(input())
print(minutes_used(drain_per_minute))
