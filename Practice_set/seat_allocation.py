"""
Bus has 40 seats. For each booking request:
If seats available → CONFIRMED


Else → WAITLISTED


Input
N
request1
request2
...
Output
CONFIRMED / WAITLISTED

Sample Input
3
15
10
20


Sample Output
CONFIRMED
CONFIRMED
WAITLISTED

Hint:
Track remaining seats.

"""
def is_available(N):
    available_seats = 40
    sum =0
    for _ in range(N):
        seats = int(input())
        if available_seats > seats:
            print("CONFIRMED")
            available_seats -= seats
        else:
            print("WAITLISTED")
N = int(input())
is_available(N)