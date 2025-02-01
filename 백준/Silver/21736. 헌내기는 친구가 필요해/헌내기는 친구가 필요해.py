import sys
from collections import deque

def bfs(row, col):
    cnt = 0
    dq = deque()
    dq.append((row, col))
    visited = [[False] * M for _ in range(N)]
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    while dq:
        r, c = dq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    if campus[nr][nc] == 'P':
                        cnt += 1
                    elif campus[nr][nc] == 'X':
                        continue
                    dq.append((nr, nc))

    if cnt:
        print(cnt)
    else:
        print("TT")

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    campus = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
    
    for r in range(N):
        for c in range(M):
            if campus[r][c] == 'I':
                bfs(r, c)