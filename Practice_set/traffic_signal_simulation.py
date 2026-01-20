"""
Traffic Signal Simulation
Problem Statement
A signal cycles every second:
1–30 → RED
31–45 → YELLOW
46–90 → GREEN

Given a time T, print the signal color.
Input:
T

Output:
RED / YELLOW / GREEN

Sample Input:
44

Sample Output:
YELLOW

Hint:
Use modulo arithmetic and range checks.

"""

def traffic_signal_simulation(time):
    time = time % 90
    if(1<= time <= 30):
        print("RED")
    elif(31 <= time <= 45):
        print("YELLOW")
    else:
        print("GREEN")

time = int(input())
traffic_signal_simulation(time)