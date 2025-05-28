import sys
from collections import deque

def bfs(row, col):
    dq = deque()
    dq.append((row, col))
    visited[row][col] = 1

    while dq:
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if cheeze[nr][nc]:
                    visited[nr][nc] += 1
                else:
                    if not visited[nr][nc]:
                        visited[nr][nc] = 1
                        dq.append((nr, nc))

def remove_cheeze():
    flag = False
    
    for r in range(N):
        for c in range(M):
            if visited[r][c] >= 2:
                cheeze[r][c] = 0
            else:
                if cheeze[r][c]:
                    flag = True
    
    if flag:
        return True
    else:
        return False
    
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    cheeze = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    time = 0

    while 1:
        visited = [[0] * M for _ in range(N)]

        bfs(0, 0)

        time += 1

        if not remove_cheeze():
            break

    print(time)