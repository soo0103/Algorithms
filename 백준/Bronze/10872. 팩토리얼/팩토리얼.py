import sys

N = int(sys.stdin.readline())

if N == 0:
    print(1)
else:
    value = 1

    for i in range(1, N + 1):
        value *= i

    print(value)