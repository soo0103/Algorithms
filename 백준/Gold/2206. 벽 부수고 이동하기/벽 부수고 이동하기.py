import sys
from collections import deque

def bfs(row, col):
    dq = deque()
    dq.append((row, col, 0))

    while dq:
        r, c, broken = dq.popleft()

        if r == N - 1 and c == M - 1:
            return visited[r][c][broken]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if guidance[nr][nc] == 1 and not broken:
                    visited[nr][nc][1] = visited[r][c][0] + 1
                    dq.append((nr, nc, 1))
                elif guidance[nr][nc] == 0 and visited[nr][nc][broken] == 0:
                        visited[nr][nc][broken] = visited[r][c][broken] + 1
                        dq.append((nr, nc, broken))

    return -1

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    guidance = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    print(bfs(0, 0))