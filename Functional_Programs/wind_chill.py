import sys 
import math
"""
    Write a program WindChill.java that takes two double command-line arguments t
    and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
    temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
    National Weather Service defines the effective temperature (the wind chill) to be:
            w = 35.74 + 0.6215 t + (0.4275 t - 35.75) v^0.16
"""
def wind_speed(t, v):
    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
    return w

t = float(sys.argv[1])   
v = float(sys.argv[2])  

result = wind_speed(t, v)
print(result)

