import sys

N = int(sys.stdin.readline())

weights = list(map(int, sys.stdin.readline().split()))
weights.sort()

dp = [0] * N

if weights[0] == 1:
    dp[0] = 1

for i in range(1, N):
    if weights[i] <= dp[i - 1] + 1:
        dp[i] = dp[i - 1] + weights[i]
    else:
        break

print(max(dp) + 1)