import sys

N = int(sys.stdin.readline())

dp = [[1] * 10 for _ in range(N)]

if N != 1:
    for i in range(1, N):
        dp[i][0] = sum(dp[i - 1])
        
        for j in range(1, 10):
            dp[i][j] = (dp[i][j - 1] - dp[i - 1][j - 1]) % 10007

print(sum(dp[-1]) % 10007)