import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[0] * 1001 for _ in range(1001)]
dp[0][0] = 1
dp[1][0] = 1
dp[1][1] = 1

for n in range(2, N + 1):
    for k in range(n + 1):
        if k == 0:
            dp[n][0] = 1
        
        if n == k:
            dp[n][k] = 1
        else:
            dp[n][k] = (dp[n - 1][k - 1] + dp[n - 1][k]) % 10007

print(dp[N][K])