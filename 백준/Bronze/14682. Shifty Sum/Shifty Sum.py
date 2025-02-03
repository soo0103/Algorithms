import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

value = 0

for i in range(k + 1):
    value += N * (10 ** i)

print(value)