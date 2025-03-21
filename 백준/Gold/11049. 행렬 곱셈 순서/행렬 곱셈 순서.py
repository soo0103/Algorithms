import sys

INF = int(1e9)

N = int(sys.stdin.readline())
matrices = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[INF] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 0

for d in range(N - 1):
    for i in range(N - d - 1):
        j = i + d + 1
        for k in range(i, j):
            value = dp[i][k] + dp[k + 1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
            if dp[i][j] > value:
                dp[i][j] = value

print(dp[0][N - 1])