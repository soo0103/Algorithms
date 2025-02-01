import sys

N, W, H = map(int, sys.stdin.readline().split())

length = (W ** 2 + H ** 2) ** 0.5

for _ in range(N):
    l = int(sys.stdin.readline())

    if l <= length:
        print("DA")
    else:
        print("NE")