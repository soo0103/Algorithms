import sys
from collections import deque

def bfs(row, col):
    dq = deque()
    dq.append((row, col))
    paper[row][col] = -1
    count = 1

    while dq:
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and paper[nr][nc] == 1:
                dq.append((nr, nc))
                paper[nr][nc] = -1
                count += 1

    return count

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    area = [0]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    for r in range(n):
        for c in range(m):
            if paper[r][c] == 1:
                cnt = bfs(r, c)
                area.append(cnt)

    print(len(area) - 1)
    print(max(area))