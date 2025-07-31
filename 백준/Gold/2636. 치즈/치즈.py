import sys
from collections import deque

def bfs(row, col):
    dq = deque()
    dq.append((row, col))
    visited[row][col] = True
    
    while dq:
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if cheese[nr][nc] == 1:
                    if not exposed[nr][nc]:
                        exposed[nr][nc] = 1
                else:
                    if not visited[nr][nc]:
                        dq.append((nr, nc))
                        visited[nr][nc] = True

def melt():
    global piece
    for i in range(N):
        for j in range(M):
            if exposed[i][j]:
                piece += 1
                cheese[i][j] = 0

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    time = 0
    pieces = []
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    while 1:
        exposed = [[0] * M for _ in range(N)]
        visited = [[False] * M for _ in range(N)]
        piece = 0

        bfs(0, 0)
        melt()

        if piece == 0:
            print(time)
            print(pieces[-1])
            break
        else:
            time += 1
            pieces.append(piece)