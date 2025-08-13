import sys

N, M = map(int, sys.stdin.readline().split())

basket = [0] * N

for l in range(M):
    i, j, k = map(int, sys.stdin.readline().split())

    for o in range(i, j + 1):
        basket[o - 1] = k
        
print(*basket)