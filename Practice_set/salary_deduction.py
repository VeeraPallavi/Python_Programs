"""
Problem Statement
Employee salary rules:
Basic salary given

If late days > 5 → deduct 5%
If late days > 10 → deduct 10%
If absent days > 2 → deduct additional 5%

Input:
salary
late_days
absent_days

Output:
final_salary

Sample Input:
50000
8
1

Sample Output:
47500

Hint:
Apply deductions cumulatively, not exclusively.
"""

def salary_deduction(salary, late_days, absent_days):
    if (5 < late_days <= 10):
        salary = salary - (salary * 0.05)
    if absent_days > 2:
        salary = salary - (salary * 0.05)
    
    return salary
salary = int(input())
late_days = int(input())
absent_days = int(input())
print(int(salary_deduction(salary, late_days, absent_days)))