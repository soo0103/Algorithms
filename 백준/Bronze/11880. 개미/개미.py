import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a, b, c = map(int, sys.stdin.readline().split())

    longest = max((a, b, c))

    distance = longest ** 2 + (a + b + c - longest) ** 2

    print(distance)