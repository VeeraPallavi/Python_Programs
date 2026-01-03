"""
Problem Statement
Tank capacity is 1000L. Inflow every minute given.
 Stop when overflow occurs and print minute number.
Input
N
inflow1 inflow2 ... inflowN
Output
overflow_minute

Sample Input
5
200 300 250 400 100
Sample Output
4

Hint :
Accumulate volume gradually.

"""
def tank_overflow(N,inflow):
    tank_capacity = 1000
    sum =0
    minute = 1
    for i in inflow:
        sum = sum + i
        if sum < tank_capacity:
            minute += 1
    print(minute)
        
N = int(input())
inflow = list(map(int, input().split()))
tank_overflow(N, inflow)
