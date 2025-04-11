import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[0] * 201 for _ in range(201)]
dp[0][0] = 1

for i in range(N + 1):
    for j in range(1, K + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000

print(dp[N][K])