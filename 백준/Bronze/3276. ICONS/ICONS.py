import sys

N = int(sys.stdin.readline())

r, c = 1, 1

while r * c < N:
    if r > c:
        c += 1
    else:
        r += 1

print(r, c)