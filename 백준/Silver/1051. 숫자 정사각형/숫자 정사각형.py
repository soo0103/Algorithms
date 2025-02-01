import sys

N, M = map(int, sys.stdin.readline().split())
num = []

for _ in range(N):
    num.append(list(map(int, sys.stdin.readline().rstrip())))

check = min(N, M)
value = 0

for i in range(N):
    for j in range(M):
        for k in range(check):
            if ((i + k) < N) and ((j + k) < M) and (num[i][j] == num[i][j + k] == num[i + k][j] == num[i + k][j + k]):
                value = max(value, (k + 1)**2)
                
print(value)