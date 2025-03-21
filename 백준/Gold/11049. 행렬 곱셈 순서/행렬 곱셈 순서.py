import sys

INF = int(1e9)

def minmult():
    for d in range(1, N + 1):
        for i in range(1, N - d + 1):
            j = i + d
            for k in range(i, j):
                value = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if dp[i][j] > value:
                    dp[i][j] = value

    print(dp[1][N])

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    matrices = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dp = [[INF] * (N + 1) for _ in range(N + 1)]
    p = [0, matrices[0][0]] + [m[1] for m in matrices]

    for i in range(N + 1):
        dp[i][i] = 0

    minmult()