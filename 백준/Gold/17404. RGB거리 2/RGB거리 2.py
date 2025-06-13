import sys

INF = int(1e9)

N = int(sys.stdin.readline())
rgb = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = INF

for i in range(3):
    dp = [[INF] * 3 for _ in range(N)]
    dp[0][i] = rgb[0][i]
    
    for j in range(1, N):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + rgb[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + rgb[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + rgb[j][2]
        
    dp[N - 1][i] = INF
    result = min(result, min(dp[N - 1]))
    
print(result)