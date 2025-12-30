import math
"""
    Write a program Distance.java that takes two integer command-line arguments x
    and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
    formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
"""
def distance(x, y):
    distance = math.sqrt(x * x + y * y)
    return distance

x = int(input("Enter X value : "))
y = int(input("Enter Y value : "))

result =distance(x, y)
print(result)
