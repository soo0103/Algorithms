import sys
from collections import deque

def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    ground[i][j] = 0

    while dq:
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and ground[nr][nc] == -1:
                if distance[nr][nc] != 0:
                    ground[nr][nc] = ground[r][c] + 1
                    dq.append((nr, nc))

                if distance[nr][nc] == 0:
                    ground[nr][nc] = 0

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    distance = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ground = [[-1] * m for _ in range(n)]
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    for i in range(n):
        for j in range(m):
            if distance[i][j] == 0:
                ground[i][j] = 0
        
    for i in range(n):
        for j in range(m):
            if distance[i][j] == 2:
                bfs(i, j)
    
    for i in ground:
        print(*i)