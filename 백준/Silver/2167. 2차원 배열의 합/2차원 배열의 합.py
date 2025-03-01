import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
K = int(sys.stdin.readline())
coordinates = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

dp = [[0] * (M + 1) for _ in range(N + 1)]

for r in range(1, N + 1):
    for c in range(1, M + 1):
        dp[r][c] = dp[r - 1][c] + dp[r][c - 1] - dp[r - 1][c - 1] + arr[r - 1][c - 1]

for i, j, x, y in coordinates:
    print(dp[x][y] + dp[i - 1][j - 1] - dp[x][j - 1] - dp[i - 1][y])