#  Find the hypotenuse of a rectangle
# formula = C = the square root of A^2 + B^2

import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")