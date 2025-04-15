import sys

N, M = map(int, sys.stdin.readline().split())
J = int(sys.stdin.readline())
locations = [int(sys.stdin.readline()) for _ in range(J)]

current = 1
distance = 0

for location in locations:
    if current > location:
        distance += current - location
        current = location
    elif current <= location and current + M - 1 >= location:
        continue
    else:
        distance += location - M + 1 - current
        current = location - M + 1

print(distance)