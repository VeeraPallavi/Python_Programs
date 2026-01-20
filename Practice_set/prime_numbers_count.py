"""
Problem Statement
Print count of prime numbers between A and B (inclusive).
Input:
A
B
Output:
prime_count

Sample Input:
10
30
Sample Output:
6

Hint:
Check divisibility up to √n.

"""
def is_prime(num):
    if num < 2:
        return False
    i = 2
    while (i * i <= num):
        if num % i == 0:
            return False
        i += 1 
    return True

def prime_count(A, B):
    count =0
    for num in range(A, B+1):
        if is_prime(num):
            count += 1
    return count

A = int(input())
B = int(input())
count = prime_count(A, B)
print(count)