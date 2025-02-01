import sys
sys.setrecursionlimit(10 ** 9)

def dfs(r, c):
    if r == N - 1 and c == M -1:
        return 1

    if dp[r][c] != -1:
        return dp[r][c]

    cnt = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M:
            if guidance[nr][nc] < guidance[r][c]:
                cnt += dfs(nr, nc)

    dp[r][c] = cnt

    return dp[r][c]

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    guidance = []
    dp = [[-1] * M for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for _ in range(N):
        guidance.append(list(map(int, sys.stdin.readline().split())))

    print(dfs(0, 0))