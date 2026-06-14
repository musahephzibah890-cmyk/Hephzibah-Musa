import math

def quadratic(a, b, c):
    x = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    y = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

    print(f"The values of x and y are\nx = {x}\ny = {y}")

quadratic(1, -2, 1)