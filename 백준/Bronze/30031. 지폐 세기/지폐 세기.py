import sys

N = int(sys.stdin.readline())

value = 0

for _ in range(N):
    w, h = map(int, sys.stdin.readline().split())

    if w == 136:
        value += 1000
    elif w == 142:
        value += 5000
    elif w == 148:
        value += 10000
    else:
        value += 50000

print(value)