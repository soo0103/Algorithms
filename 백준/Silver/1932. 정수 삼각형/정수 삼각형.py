import sys

n = int(sys.stdin.readline())

dp = []

for _ in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))

for r in range(1, n):
    for c in range(len(dp[r])):
        if c == 0:
            dp[r][c] = dp[r - 1][c] + dp[r][c]
        elif c == len(dp[r]) - 1:
            dp[r][c] = dp[r - 1][c - 1] + dp[r][c]
        else:
            dp[r][c] = max(dp[r - 1][c - 1], dp[r - 1][c]) + dp[r][c]

print(max(dp[n - 1]))