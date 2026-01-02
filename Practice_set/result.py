"""
Problem Statement
Input marks for 5 subjects:
If any mark < 35 → FAIL
Else average ≥ 75 → DISTINCTION
Else PASS
Input
m1 m2 m3 m4 m5
Output
FAIL / PASS / DISTINCTION

Sample Input
80 78 74 90 88
Sample Output
DISTINCTION

Hint:
First validate failure condition, then classify.

"""
def result_processor(m1, m2, m3, m4, m5):
    average = (m1 + m2 + m3 + m4 + m5)/5
    if (m1 < 35) or (m2 < 35) or (m3 < 35) or (m4 < 35) or (m5 < 35):
        print("FAIL")
    elif average >= 75:
        print("DISTINCTION")
    else:
        print("PASS")

m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())
result_processor(m1, m2, m3, m4, m5)
