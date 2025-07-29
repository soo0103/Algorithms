import sys
from collections import deque

def bfs(row, col):
    global cnt
    dq = deque()
    dq.append((row, col))
    visited[row][col] = True

    while dq:
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if not iceberg[nr][nc]:
                    melted[r][c] += 1
                else:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        dq.append((nr, nc))

def melt():
    for i in range(N):
        for j in range(M):
            if melted[i][j] >= 1:
                if iceberg[i][j] - melted[i][j] < 0:
                    iceberg[i][j] = 0
                else:
                    iceberg[i][j] -= melted[i][j]

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    iceberg = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    time = 0

    while 1:
        visited = [[False] * M for _ in range(N)]
        melted = [[0] * M for _ in range(N)]
        cnt = 0

        for i in range(N):
            for j in range(M):
                if iceberg[i][j] and not visited[i][j]:
                    bfs(i, j)
                    cnt += 1
        
        melt()

        if cnt >= 2:
            break
        elif cnt == 0:
            time = 0
            break
        else:
            time += 1

    print(time)