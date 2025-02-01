import sys

def dfs1(r, c, cnt, num):
    global value

    if cnt == 4:
        value = max(num, value)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs1(nr, nc, cnt + 1, num + tetro[nr][nc])
            visited[nr][nc] = False

def dfs2(r, c):
    global value
    val = tetro[r][c]
    exc = 1001

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < M: 
            exc = min(exc, tetro[nr][nc])
            val += tetro[nr][nc]
        else:
            exc = 0

    val -= exc
    value = max(value, val)

    return

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    tetro = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    value = 0
    cnt = 1
    visited = [[False] * M for _ in range(N)]

    for j in range(N):
        for i in range(M):
            visited[j][i] = True
            dfs1(j, i, cnt, tetro[j][i])
            dfs2(j, i)
            visited[j][i] = False
            
    print(value)