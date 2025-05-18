import sys

N, M = map(int, sys.stdin.readline().split())
maze = [[0] * M]

for _ in range(N):
    maze.append([0] + list(map(int, sys.stdin.readline().split())))

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + maze[i][j]

print(dp[N][M])