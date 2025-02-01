import sys

T = int(sys.stdin.readline())
dp = [[0] * 31 for _ in range(31)]

for i in range(1, 31):
    for j in range(1, 31):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    
    print(dp[N][M])