import sys

N, M = map(int, sys.stdin.readline().split())
seq = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

basket = [i for i in range(N + 1)]

for i, j in seq:
    while i <= j:
        basket[i], basket[j] = basket[j], basket[i]
        i += 1
        j -= 1

print(*basket[1:])