import sys

T = int(sys.stdin.readline())

dp = [1] * 101

for _ in range(T):
    N = int(sys.stdin.readline())

    for i in range(4, N + 1):
        dp[i] = dp[i - 2] + dp[i - 3]
    
    print(dp[N])