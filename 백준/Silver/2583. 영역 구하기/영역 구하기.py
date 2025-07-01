import sys
from collections import deque

def bfs(row, col):
    dq = deque()
    dq.append((row, col))
    count = 1
    field[row][col] = -1

    while dq:
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < M and 0 <= nc < N and field[nr][nc] == 0:
                field[nr][nc] = -1
                dq.append((nr, nc))
                count += 1

    area.append(count)
    
if __name__ == "__main__":
    M, N, K = map(int, sys.stdin.readline().split())
    rectangles = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

    field = [[0] * N for _ in range(M)]
    area = []

    for rectangle in rectangles:
        x1, y1, x2, y2 = rectangle

        for y in range(y1, y2):
            for x in range(x1, x2):
                field[y][x] = 1

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    for r in range(M):
        for c in range(N):
            if field[r][c] == 0:
                bfs(r, c)

    area.sort()

    print(len(area))
    print(*area)