import sys

X, Y, D, T = map(int, sys.stdin.readline().split())

distance = (X ** 2 + Y ** 2) ** 0.5

if distance >= D:
    time = min((distance // D) * T + distance % D, distance, (distance // D + 1) * T)
else:
    time = min(T + D - distance, distance, 2 * T)

print(time)