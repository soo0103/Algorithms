import sys
from collections import deque

def bfs(row, col):
    dq = deque()
    dq.append((row, col))

    while dq:
        r, c = dq.popleft()

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and guidance[nr][nc]:
                guidance[nr][nc] = -1
                visited[nr][nc] = True
                dq.append((nr, nc))

if __name__ == "__main__":
    while 1:
        w, h = map(int, sys.stdin.readline().split())

        if w == h == 0:
            break

        guidance = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
        visited = [[False] * w for _ in range(h)]
        cnt = 0

        dr = [1, 0, -1, 0, 1, 1, -1, -1]
        dc = [0, 1, 0, -1, 1, -1, 1, -1]

        for r in range(h):
            for c in range(w):
                if not visited[r][c] and guidance[r][c]:
                    visited[r][c] = True
                    bfs(r, c)
                    cnt += 1

        print(cnt)