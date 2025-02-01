import sys

N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for r in range(N):
    for c in range(M):
        print(A[r][c] + B[r][c], end = ' ')
    print()