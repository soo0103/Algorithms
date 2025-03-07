import sys

a, b = map(int, sys.stdin.readline().split())

if a <= 2:
    a = 3

if a % 2:
    a += 1

if b % 2:
    b -= 1

a //= 2
b //= 2

if a > b:
    print(0)
else:
    print(b * (b + 1) - a * (a - 1))