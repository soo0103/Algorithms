import sys

N, M = map(int, sys.stdin.readline().split())

matrix = [[100] * N for _ in range(N)]
friend = [0] * N
INF = int(1e9)
min_value = INF

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    matrix[A - 1][B - 1] = 1
    matrix[B - 1][A - 1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j:
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
            else:
                matrix[i][j] = 0

for i in range(N):
    friend[i] = sum(matrix[i])

for i in range(N):
    if friend[i] < min_value:
        min_value = sum(matrix[i])
    
for i in range(N):
    if friend[i] == min_value:
        print(i + 1)
        break