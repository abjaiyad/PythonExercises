# calculate the circumference of a circle
# formula = C = 2 pi r

import math

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference of the circle with radius {radius} is {round(circumference, 2)}cm")