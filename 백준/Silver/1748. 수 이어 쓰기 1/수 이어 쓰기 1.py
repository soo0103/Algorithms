import sys

N = int(sys.stdin.readline())

num = 0
i = 1

while i <= N:
    num += N - i + 1
    i *= 10

print(num)