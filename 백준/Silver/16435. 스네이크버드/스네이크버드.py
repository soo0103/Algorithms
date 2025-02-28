import sys

N, L = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))

heights.sort()

for i in range(N):
    if heights[i] <= L:
        L += 1
    
print(L)