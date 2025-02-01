import sys

N = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][k] != 0 and matrix[k][j] != 0:
                matrix[i][j] = 1

for i in matrix:
    print(*i)