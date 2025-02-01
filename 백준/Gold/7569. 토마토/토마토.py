import sys
from collections import deque

def bfs():
    while dq:
        x, y, z = dq.popleft()
        
        for i in range(6):
            nx = x + dx[i] 
            ny = y + dy[i]
            nz = z + dz[i]
            
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if tomato[nz][ny][nx] == 0:
                    dq.append((nx, ny, nz))
                    tomato[nz][ny][nx] = tomato[z][y][x] + 1

    return

if __name__ == "__main__":
    M, N, H = map(int, sys.stdin.readline().split())
    tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
    dq = deque()
    day = 0
    dx = [1, -1, 0, 0, 0, 0] 
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    for k in range(H):
        for j in range(N):
            for i in range(M):
                if tomato[k][j][i] == 1:
                    dq.append((i, j, k))

    bfs()

    for c in tomato:
        for b in c:
            for a in b:
                if a == 0:
                    print(-1)
                    exit(0)

            day = max(day, max(b))
            
    print(day - 1)