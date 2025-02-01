import sys

D, H, W = map(int, sys.stdin.readline().split())

c = (H ** 2 + W ** 2) ** 0.5

ratio = D / c

print(int(H * ratio), int(W * ratio))