import math

a = float(input())
b = float(input())
c = float(input())

delta = b**2 -4*a*c

sraiz = (-b - math.sqrt(delta)) / (2*a)

print("%.2f" %sraiz)