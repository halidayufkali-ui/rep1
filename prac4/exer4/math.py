import math

# Degree to radian
degree = float(input())
print(round(degree * math.pi / 180))

# Trapezoid area
h = float(input())
b1 = float(input( ))
b2 = float(input())
print( 0.5 * (b1 + b2) * h)

# Regular polygon area
n = int(input())
a = float(input())
area_poly = a**2 if n == 4 else (n * a**2) / (4 * math.tan(math.pi / n))
print(area_poly)

# Parallelogram area
base = float(input())
height = float(input())
print( base * height)