import sys
import math

x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().split())

d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if d >= r1 + r2:
    area = 0
elif d <= abs(r1 - r2):
    area = math.pi * min(r1, r2) ** 2
else:
    theta1 = 2 * math.acos((r1 ** 2 + d ** 2 - r2 ** 2) / (2 * r1 * d))
    theta2 = 2 * math.acos((r2 ** 2 + d ** 2 - r1 ** 2) / (2 * r2 * d))

    a1 = 0.5 * r1 ** 2 * (theta1 - math.sin(theta1))
    a2 = 0.5 * r2 ** 2 * (theta2 - math.sin(theta2))

    area = a1 + a2

print(f"{area:.3f}")