import sys

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * (N + 1) for _ in range(N + 1)]

for r in range(1, N + 1):
    for c in range(1, N + 1):
        dp[r][c] = dp[r - 1][c] + dp[r][c - 1] - dp[r - 1][c - 1] + graph[r - 1][c - 1]
    
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])