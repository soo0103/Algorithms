import sys

X1, Y1, R1 = map(int, sys.stdin.readline().split())
X2, Y2, R2 = map(int, sys.stdin.readline().split())

r = R1 + R2
d = ((X2 - X1) ** 2 + (Y2 - Y1) ** 2) ** 0.5

if d < r:
    print("YES")
else:
    print("NO")