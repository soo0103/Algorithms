import sys
from collections import deque
from copy import deepcopy

def bfs(row, col, h):
    dq = deque()
    dq.append((row, col))

    while dq:
        r, c = dq.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not sunk[nr][nc]:
                if zone[nr][nc] <= h:
                    sunk[nr][nc] = True
                    dq.append((nr, nc))

def getSafe(row, col):
    dq = deque()
    dq.append((row, col))

    while dq:
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not sunk[nr][nc]:
                if zone[nr][nc] != -1:
                    zone[nr][nc] = -1
                    dq.append((nr, nc))

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    height = max(map(max, area))
    count = 0
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    for h in range(height + 1):
        zone = deepcopy(area)
        sunk = [[False] * N for _ in range(N)]
        cnt = 0

        for r in range(N):
            for c in range(N):
                if not sunk[r][c] and zone[r][c] <= h:
                    sunk[r][c] = True
                    bfs(r, c, h)

        for r in range(N):
            for c in range(N):
                if not sunk[r][c] and zone[r][c] != -1:
                    zone[r][c] = -1
                    getSafe(r, c)
                    cnt += 1

        count = max(cnt, count)

    print(count)