import math

"""
    Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
    Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
    can be found using a formula (Note: Take a, b and c as input values)
    delta = b*b - 4*a*c
    Root 1 of x = (-b + sqrt(delta))/(2*a)
    Root 2 of x = (-b - sqrt(delta))/(2*a)
"""
def roots(a, b, c):
    delta = b ** 2 - (4 * a * c)
    if delta == 0:
        print("Roots are equal")
        root = -b / (2 * a)
    elif delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print(root1)
        print(root2)
    else:
        print("Roots are imaginary")


a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
c = int(input("Enter c value : "))

roots(a, b, c)