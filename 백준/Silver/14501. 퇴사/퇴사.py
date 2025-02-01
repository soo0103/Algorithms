import sys

N = int(sys.stdin.readline())
dp = [0] * (N + 1)
counseling = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N - 1, -1, -1):
    if i + counseling[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + counseling[i][0]] + counseling[i][1])

print(dp[0])