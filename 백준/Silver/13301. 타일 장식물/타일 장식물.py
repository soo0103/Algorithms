import sys

N = int(sys.stdin.readline())

dp = [0] * 81

dp[1] = 1
dp[2] = 1

for i in range(3, 81):
    dp[i] = dp[i - 1] + dp[i - 2]

if N == 1:
    result = 4
elif N == 2:
    result = 6
elif N == 3:
    result = 10
else:
    result = dp[N] * 3 + dp[N - 1] * 2 + dp[N - 2] * 2 + dp[N - 3]

print(result)